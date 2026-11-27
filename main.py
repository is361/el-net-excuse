import os
text = "I missed the deadline by one hour, and I want you to know it was the most intentional hour I've ever spent."
open(os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8").write(text)
