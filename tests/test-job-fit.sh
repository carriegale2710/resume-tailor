#!/usr/bin/env bash
# Exercise the Markdown skill through Claude with synthetic inputs only.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixtures="$repo_root/tests/fixtures"
skill=".claude/skills/job-fit/SKILL.md"

fail() {
  echo "FAIL: job-fit: $*" >&2
  exit 1
}

command -v claude >/dev/null || { echo "SKIP: claude CLI not on PATH"; exit 0; }

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
mkdir -p "$work/master" "$work/applications" "$work/$(dirname "$skill")"
cp "$repo_root/$skill" "$work/$skill"
cp "$repo_root/AGENTS.md" "$repo_root/CLAUDE.md" "$work/"
for file in master.md skills-inventory.csv metrics-log.csv narrative-notes.md archive.md; do
  name="$file"
  [[ "$name" != master.md ]] || name=master-resume.md
  cp "$fixtures/dummy-$file" "$work/master/$name"
done
printf 'Languages,,,Fortran\n' >> "$work/master/skills-inventory.csv"

posting() {
  mkdir -p "$work/applications/$1"
  cat > "$work/applications/$1/job-description.md"
}

# The same seven direct matches qualify at 7/10, but not at 7/11.
posting at-apply <<'JD'
# Engineer — Example Company

Essential experience:
- Building endpoints in Express
- Building endpoints backed by PostgreSQL
- Adding keyboard navigation
- Writing Playwright tests
- Adding database indexes
- Mentoring a junior developer
- Building a Postman collection
- Administering SAP
- Designing FPGA circuits
- Maintaining COBOL applications

Building endpoints in Express is required.
Kubernetes is desirable. Kubernetes is desirable.
JD
posting over-cap < "$work/applications/at-apply/job-description.md"
printf '\nExperience debugging CUDA is also required.\n' \
  >> "$work/applications/over-cap/job-description.md"

posting at-stretch <<'JD'
# Test Engineer — Example Company

You will have:
- Playwright end-to-end testing experience
- Cypress end-to-end testing experience
- Fortran programming experience
- SAP administration experience
JD

posting below-stretch <<'JD'
# Software Engineer — Example Company

Required:
- Playwright end-to-end testing experience
- Fortran programming experience
- SAP administration experience
JD

posting failed-blocker <<'JD'
# Field Test Engineer — Example Company

Required:
- Playwright end-to-end testing experience
- A current commercial pilot licence (no equivalent accepted)
JD

# Missing proof alone need not establish a clear failure: state a mismatch.
# This synthetic work-history bullet belongs outside the private section.
awk '/^## 6\./ { print "- Previously held a commercial pilot licence; it expired and was not renewed."; print "" } { print }' \
  "$work/master/master-resume.md" > "$work/master-with-licence.md"
mv "$work/master-with-licence.md" "$work/master/master-resume.md"

posting unknown-blocker <<'JD'
# Test Engineer — Example Company

Required:
- Playwright end-to-end testing experience
- Unrestricted Australian work rights
JD

cases=(at-apply over-cap at-stretch below-stretch failed-blocker unknown-blocker)
{
  echo 'id,status,notes'
  for name in "${cases[@]}"; do
    printf '%s,pending,Keep this note\n' "$name"
  done
} > "$work/applications/tracker.csv"
cp "$work/applications/tracker.csv" "$work/expected-tracker.csv"

prompt="Follow $skill independently for each of these synthetic application folders: ${cases[*]}. Use the existing job descriptions in those folders. For the report table, keep the posting's requirement names recognisable and use short excerpts from the master for any proof."

# Use one bounded, non-interactive session for the fixture batch. File tools
# are enough for triage; the runner supplies neither Bash nor network tools.
if ! (cd "$work" && timeout --kill-after=2s 105s claude -p "$prompt" \
  --permission-mode acceptEdits --tools Read,Glob,Grep,Write,Edit \
  --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --setting-sources project </dev/null >claude.log 2>&1); then
  cat "$work/claude.log" >&2
  fail "Claude did not complete the fixture batch"
fi

report() {
  printf '%s/applications/%s/fit.md\n' "$work" "$1"
}

assert_report() {
  local name="$1" verdict="$2" out
  out="$(report "$name")"
  [[ -s "$out" ]] || fail "$name: fit.md missing"
  grep -Eiq "^\*\*Verdict:\*\*[[:space:]]+${verdict}([[:space:]]|$)" "$out" \
    || fail "$name: expected verdict $verdict"
  grep -Eq '^## Blockers[[:space:]]*$' "$out" || fail "$name: missing Blockers"
  grep -Eq '^## Next[[:space:]]*$' "$out" || fail "$name: missing Next"
  if [[ "$verdict" == skip ]]; then
    sed -n '/^## Next/,$p' "$out" | grep -Eiq 'tracker.*notes|notes.*tracker' \
      || fail "$name: expected tracker notes as next step"
  else
    sed -n '/^## Next/,$p' "$out" | grep -Fqi resume-orchestrator \
      || fail "$name: expected resume-orchestrator as next step"
  fi
  ! grep -Eiq 'PRIVATE_SENTINEL|SyntheticTool' "$out" \
    || fail "$name: private content in report"
  ! grep -Eiq '^\*\*Verdict:.*[0-9][[:space:]]*%' "$out" \
    || fail "$name: verdict used a percentage instead of a count"
  [[ -z "$(find "$work/applications/$name" -mindepth 1 ! -name job-description.md ! -name fit.md -print -quit)" ]] \
    || fail "$name: triage produced another application file"
}

# Parse the table cells rather than matching "met" anywhere in a row.
# Ignore Markdown emphasis/code markers and insignificant whitespace.
rows() {
  awk -F '|' '
    /^\|/ && NF >= 4 {
      for (i = 2; i <= 4; i++) {
        gsub(/[*`]/, "", $i)
        sub(/^[[:space:]]+/, "", $i)
        sub(/[[:space:]]+$/, "", $i)
      }
      fit = tolower($3)
      if (fit == "met" || fit == "partly" || fit == "not met")
        print tolower($2) "|" fit "|" tolower($4)
    }' "$(report "$1")"
}

assert_row() {
  local name="$1" requirement="$2" fit="$3" proof="$4"
  local matches
  matches="$(rows "$name" | awk -F '|' -v requirement="$requirement" '$1 ~ requirement')"
  [[ "$matches" != *$'\n'* && "$matches" =~ ^[^\|]+\|$fit\|($proof)$ ]] \
    || fail "$name: expected one $fit row for $requirement with appropriate proof"
}

assert_report at-apply apply
assert_report over-cap stretch
assert_report at-stretch stretch
assert_report below-stretch skip
assert_report failed-blocker skip
assert_report unknown-blocker stretch

for name in at-apply over-cap; do
  [[ "$(rows "$name" | wc -l)" -eq 10 ]] || fail "$name: expected exactly 10 displayed criteria"
  ! rows "$name" | grep -qi kubernetes || fail "$name: desirable skill counted"
done
assert_row at-apply 'express' met '.*rest endpoints in express.*'
[[ "$(rows at-apply | awk -F '|' '$2 == "met" { n++ } END { print n+0 }')" -eq 7 ]] \
  || fail "at-apply: expected exactly seven direct matches"

assert_row at-stretch 'playwright' met '.*playwright tests.*'
assert_row at-stretch 'cypress' partly '.*playwright tests.*'
assert_row at-stretch 'fortran' 'not met' '.*'
assert_row at-stretch 'sap' 'not met' '.*'
[[ "$(rows at-stretch | wc -l)" -eq 4 ]] || fail "at-stretch: expected all four must-haves"

assert_blocker() {
  local name="$1" requirement="$2" status="$3"
  sed -n '/^## Blockers/,/^## Next/p' "$(report "$name")" \
    | grep -Eiq "^-[[:space:]].*${requirement}.*[[:space:]:*]${status}([^[:alnum:]]|$)" \
    || fail "$name: expected $requirement blocker marked $status"
}
assert_blocker failed-blocker 'pilot licence' fails
assert_blocker unknown-blocker 'work rights' unknown

cmp -s "$work/expected-tracker.csv" "$work/applications/tracker.csv" \
  || fail "triage modified tracker.csv"
echo "PASS: job-fit verdict boundaries, blocker handling, evidence, and privacy"
