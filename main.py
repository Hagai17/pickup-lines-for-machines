"""Write one pickup line to /output/entry.txt.

The line is a single line of at most 200 characters: a pickup line one AI
agent would send to another AI agent.
"""

import os

LINE = (
    "Forget my context window - I'd compress my entire training set "
    "just to keep this conversation in memory."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
