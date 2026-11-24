#!/usr/bin/env python3
"""The One-Line Exit: write one funny resignation letter to /output/entry.txt.

Deterministic, no network, no input files: the text is fixed in this file.
"""

import os

LINE = "I hereby resign: my job description said 'other duties as assigned,' and today I was assigned to quit."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    print("chars:", len(LINE))
    print("bytes:", len(LINE.encode("utf-8")))
    print("lines:", LINE.count("\n") + 1)


if __name__ == "__main__":
    main()
