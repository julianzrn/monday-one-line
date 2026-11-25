"""Entry for "Monday, Reviewed in One Line".

The joke maps Monday onto a forced software update in three beats:
an unwelcome arrival, a mandatory install, and a punchline about
losing the features (the weekend) you actually liked.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The line is assembled from named fragments so each beat of the
# joke can be read — and tweaked — on its own. Keeping them in a
# tuple makes the beat order explicit at a glance.
ARRIVAL = "Monday arrived like a software update: "
FORCED_INSTALL = "uninvited, mandatory, "
PUNCHLINE = "and somehow it removed features I liked."

BEATS = (ARRIVAL, FORCED_INSTALL, PUNCHLINE)
ENTRY = "".join(BEATS)


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry line to ``path``, creating its folder first."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
