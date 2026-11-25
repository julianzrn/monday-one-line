from pathlib import Path

ENTRY = (
    "Monday arrived like a software update: uninvited, mandatory, "
    "and somehow it removed features I liked."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
