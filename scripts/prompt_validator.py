"""
Prompt Template Validator
Checks that XML-structured Markdown prompts contain required tags (<role>, <task>).
"""
import sys
import re
from pathlib import Path

REQUIRED_TAGS = ["role", "task"]

def validate_prompt_file(file_path: str) -> bool:
    path = Path(file_path)
    if not path.exists():
        print(f"[ERROR] File not found: {file_path}")
        return False

    content = path.read_text(encoding="utf-8")
    missing = []
    for tag in REQUIRED_TAGS:
        pattern = rf"<{tag}>.*?</{tag}>"
        if not re.search(pattern, content, re.DOTALL):
            missing.append(tag)

    if missing:
        print(f"[FAIL] {path.name} is missing XML tags: {', '.join(missing)}")
        return False

    print(f"[PASS] {path.name} is valid and properly structured.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python prompt_validator.py <path_to_markdown_file>")
        sys.exit(1)
    success = validate_prompt_file(sys.argv[1])
    sys.exit(0 if success else 1)
