"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one original one-line office joke to /output/entry.txt.
The joke: a boss asks for a five-year plan, and the calendar answers —
the same meeting, every week, until retirement. The turn is the plan
itself: not a ladder, just the meeting, repeated.
"""

from pathlib import Path

JOKE = "My boss asked for my five-year plan, so I showed him my calendar: this meeting, every week, until I retire."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate rejects non-UTF-8, empty/whitespace-only, or >=200-char
    # text, so normalise once and validate before writing anything.
    joke = " ".join(JOKE.split())
    assert "\n" not in joke, "joke must be a single line"
    assert 1 <= len(joke) <= 199, f"joke must be 1-199 chars, got {len(joke)}"
    assert joke.strip(), "joke must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")
    print(f"Wrote one-line joke ({len(joke)} chars) to {OUTPUT_PATH}")
    print(joke)


if __name__ == "__main__":
    main()
