"""One-star review of something essential.

A deterministic program that writes one deadpan one-star review line
to /output/entry.txt and prints it to stdout.
"""

import os

LINE = "★☆☆☆☆ Time: non-refundable, no pause button, and customer support is a clock that just keeps going."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the review line to /output/entry.txt and print it."""
    assert 1 <= len(LINE) <= 160, "line must be 1-160 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
