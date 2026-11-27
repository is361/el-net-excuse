import os

TEXT = "I missed the deadline by one hour, and I want you to know it was the most intentional hour I've ever spent."

def main() -> None:
    out = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")
    assert 1 <= len(TEXT) <= 200, "entry text must be 1-200 characters"
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)

main()
