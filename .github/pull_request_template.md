<!-- 
  =============================================================================
  NOTE: This repository enforces SQUASH MERGING.
  When this PR is merged, GitHub squashes all commits into a single commit on `main`.
  The PR Title will become the primary commit message headline on `main`.

  PR Title Convention:
    <tag>(<optional-scope>): <concise descriptive summary>
    or:
    [<tag>] <concise descriptive summary>

  Accepted Tags (GitHub default tags & semantic types):
    - enhancement / feat: New gameplay mechanics, episodes, levels, or features
    - bug / fix: Glitch fixes, collision patches, or issue resolutions
    - documentation / docs: Readme, manuals, guides, or documentation
    - chore: Routine maintenance, asset cleanup, or dependency updates
    - refactor: Structural changes or code reorganization without gameplay changes
    - test: Verification scripts, test episodes, or test suite additions
    - ci: GitHub Actions workflows, CI scripts, or automation

  Examples:
    enhancement(levels): add subterranean secret passage in level 4
    bug(physics): fix collision clipping during sprint jump
    [documentation] update manual with warp whistle mechanics
    ci(actions): add pull request format verification workflow
  =============================================================================
-->

## 📋 Summary
<!-- Provide a concise summary of the purpose and rationale behind this pull request. -->

## 🏷️ Type of Change
<!-- Select all relevant options by placing an 'x' inside the brackets: [x] -->
- [ ] `enhancement` / `feat` (New feature, level, or gameplay asset)
- [ ] `bug` / `fix` (Bug fix or gameplay glitch resolution)
- [ ] `documentation` / `docs` (Updates to documentation, guides, or manuals)
- [ ] `chore` (Routine maintenance, file deduplication, or asset cleanup)
- [ ] `refactor` (Restructuring without altering gameplay behavior)
- [ ] `test` (Testing scripts, verification tools, or test levels)
- [ ] `ci` (Continuous Integration, GitHub Actions, or automation)

## 💡 Context & Motivation
<!-- Why is this change necessary? What issue or feature does it address? -->

## 🔍 Key Changes
<!-- Provide a clear bulleted list of the specific changes made in this PR -->
- 

## 🧪 Testing & Verification
<!-- Describe the testing methods used to ensure this PR does not introduce regressions -->
- [ ] Verified inside TheXTech engine (`./smbx`)
- [ ] Verified naming standards with repository linter (`lint-naming.yml`)
- [ ] Verified audio format compliance (`lint-audio.yml`)
- [ ] Other manual/automated verification (specify below):

## ✅ PR Checklist
<!-- Verify each requirement before marking the PR as ready for review -->
- [ ] My PR title follows the tag format (e.g., `enhancement(scope): description` or `[bug] description`).
- [ ] My PR title is clear, concise, and ready to serve as the squashed commit message on `main`.
- [ ] I have selected the appropriate change type tag(s) above.
- [ ] No extraneous, temporary, backup, or stray editor files are included.
- [ ] All automated CI checks pass successfully.
