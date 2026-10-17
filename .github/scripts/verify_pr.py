#!/usr/bin/env python3
"""
Pull Request Title and Format Verifier for GitHub Actions.

Ensures PR titles and bodies comply with squash merging conventions and
GitHub default tags (enhancement, bug, documentation) alongside standard
semantic types (feat, fix, docs, chore, etc.).
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error

# Allowed tags: GitHub default labels and standard semantic types
ALLOWED_TAGS = {
    # Default GitHub labels / aliases
    "enhancement", "bug", "documentation",
    # Conventional commit types
    "feat", "fix", "docs",
    # Maintenance / engineering types
    "chore", "refactor", "test", "ci", "perf", "build", "style"
}

# Mapping between tags/types and GitHub repository labels
TAG_MAP_TO_GITHUB_LABEL = {
    "enhancement": "enhancement",
    "feat": "enhancement",
    "bug": "bug",
    "fix": "bug",
    "documentation": "documentation",
    "docs": "documentation",
}

# Regex to match:
#   1. tag(scope): subject
#   2. tag: subject
#   3. [tag(scope)] subject
#   4. [tag] subject
TAG_REGEX = re.compile(
    r"^(?:\[(?P<tag_bracket>[a-zA-Z_-]+)(?:\((?P<scope_bracket>[a-zA-Z0-9_\-\/]+)\))?\]|(?P<tag_plain>[a-zA-Z_-]+)(?:\((?P<scope_plain>[a-zA-Z0-9_\-\/]+)\))?:)\s+(?P<subject>.+)$"
)


def validate_pr(title: str, body: str) -> tuple[bool, list[str], dict]:
    """
    Validate PR title and body.
    Returns (is_valid, error_list, parsed_metadata).
    """
    errors = []
    metadata = {}
    cleaned_title = (title or "").strip()

    if not cleaned_title:
        errors.append("PR Title is empty.")
        return False, errors, metadata

    match = TAG_REGEX.match(cleaned_title)
    if not match:
        errors.append(
            f'PR Title "{cleaned_title}" does not follow the required tag format.\n'
            "Expected format:\n"
            "  <tag>(<scope>): <summary>  OR  [<tag>] <summary>\n"
            "Examples:\n"
            "  - enhancement(levels): add subterranean secret passage in level 2\n"
            "  - bug(physics): fix collision clipping during sprint\n"
            "  - [documentation] update gameplay guide"
        )
    else:
        tag = (match.group("tag_bracket") or match.group("tag_plain")).lower()
        scope = match.group("scope_bracket") or match.group("scope_plain")
        subject = match.group("subject").strip()

        metadata = {"tag": tag, "scope": scope, "subject": subject}

        if tag not in ALLOWED_TAGS:
            allowed_list = ", ".join(sorted(ALLOWED_TAGS))
            errors.append(
                f'Unknown tag "{tag}". Allowed tags are:\n  {allowed_list}'
            )
        elif len(subject) < 3:
            errors.append(
                f'PR subject "{subject}" is too short (minimum 3 characters required).'
            )

    # Validate PR description / body
    cleaned_body = re.sub(r"<!--.*?-->", "", body or "", flags=re.DOTALL).strip()
    if not cleaned_body:
        errors.append(
            "PR description is empty. Please complete the PR template sections "
            "(Summary, Type of Change, Key Changes, Testing)."
        )

    return len(errors) == 0, errors, metadata


def sync_github_label(repo: str, pr_number: int, target_label: str, token: str):
    """Attempt to apply the corresponding GitHub default label to the PR."""
    if not (repo and pr_number and target_label and token):
        return

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/labels"
    data = json.dumps({"labels": [target_label]}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "PR-Format-Verifier",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status in (200, 201):
                print(f'🏷️  Successfully applied default GitHub label "{target_label}" to PR #{pr_number}.')
    except Exception as ex:
        print(f'⚠️  Could not auto-apply label "{target_label}": {ex} (non-fatal)')


def run_self_tests() -> int:
    """Run internal test suite for title and body validation."""
    print("🧪 Running internal validation tests...\n")
    test_cases = [
        ("enhancement(levels): add underground secret passage", "Valid body text", True),
        ("bug: resolve player clipping through blocks", "Valid body text", True),
        ("[documentation] update gameplay guide", "Valid body text", True),
        ("feat(physics): adjust gravity constants", "Valid body text", True),
        ("fix(audio): remove mp3 references", "Valid body text", True),
        ("chore: clean up stray files", "Valid body text", True),
        ("ci(actions): add pr verification workflow", "Valid body text", True),
        ("[bug(levels)] fix exit pipe warp", "Valid body text", True),
        ("random title without tag", "Valid body text", False),
        ("invalid_tag: some description", "Valid body text", False),
        ("fix:", "Valid body text", False),
        ("feat(): missing scope content", "Valid body text", False),
        ("enhancement: valid title", "", False),  # Empty body
        ("enhancement: valid title", "<!-- only html comments -->", False),  # Empty after stripping
    ]

    passed = 0
    for title, body, expected in test_cases:
        is_valid, errors, _ = validate_pr(title, body)
        if is_valid == expected:
            passed += 1
            print(f"  ✅ PASS: \"{title}\" -> Expected valid={expected}")
        else:
            print(f"  ❌ FAIL: \"{title}\" -> Expected valid={expected}, got {is_valid}")
            for err in errors:
                print(f"     Reason: {err}")

    print(f"\nTest Summary: {passed}/{len(test_cases)} tests passed.")
    return 0 if passed == len(test_cases) else 1


def main():
    if "--test" in sys.argv:
        sys.exit(run_self_tests())

    event_path = os.environ.get("EVENT_PATH")
    if not event_path or not os.path.exists(event_path):
        print("::error::Missing or inaccessible GITHUB_EVENT_PATH environment variable.")
        sys.exit(1)

    with open(event_path, "r", encoding="utf-8") as f:
        event = json.load(f)

    pr = event.get("pull_request")
    if not pr:
        print("::error::Event payload does not contain pull_request data.")
        sys.exit(1)

    title = pr.get("title", "")
    body = pr.get("body", "")
    pr_number = pr.get("number")
    repo = event.get("repository", {}).get("full_name", "")

    print("==================================================")
    print(f"🔍 Validating Pull Request #{pr_number}")
    print(f"📌 Repository : {repo}")
    print(f'📌 PR Title   : "{title}"')
    print("==================================================")

    is_valid, errors, metadata = validate_pr(title, body)

    if is_valid:
        tag = metadata.get("tag", "")
        scope = metadata.get("scope")
        subject = metadata.get("subject", "")
        print(f"✅ Tag    : {tag}")
        print(f'✅ Scope  : {scope if scope else "(none)"}')
        print(f"✅ Subject: {subject}")

        # Attempt to synchronize default GitHub label
        token = os.environ.get("GITHUB_TOKEN")
        target_label = TAG_MAP_TO_GITHUB_LABEL.get(tag)
        current_labels = [label.get("name") for label in pr.get("labels", [])]

        if target_label and target_label not in current_labels:
            sync_github_label(repo, pr_number, target_label, token)

        print("==================================================")
        print("🎉 Pull Request format checks passed successfully!")
        print("==================================================")
        sys.exit(0)
    else:
        print("❌ Pull Request validation failed:")
        for err in errors:
            print(f"::error::{err}")
        print("\n💡 Why this matters:")
        print("  This repository enforces Squash Merging.")
        print("  The PR title will become the squashed commit headline on the main branch.")
        print("  Maintaining tagged, semantic titles guarantees clean and searchable git history.")
        print("==================================================")
        sys.exit(1)


if __name__ == "__main__":
    main()
