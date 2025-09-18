#!/usr/bin/env python3
import argparse
import csv
from datetime import date
from pathlib import Path

README_TEMPLATE = """# {title}

**Created by:** {author}  
**Date:** {today}  
**Version:** v01  

## Description
{description}

## Methodology
{methodology}

## Data Structure
See `data_dictionary.csv` for column definitions.

## Quality Assurance
{qa}

## License / Rights
{license}

## Contact
{contact}
"""

DICTIONARY_HEADERS = ["name", "type", "unit", "description", "allowed_values", "missing_values"]


def write_readme(path: Path, context: dict):
    content = README_TEMPLATE.format(**context)
    path.write_text(content, encoding="utf-8")


def write_dictionary(path: Path):
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=DICTIONARY_HEADERS)
        writer.writeheader()


def main():
    parser = argparse.ArgumentParser(description="Generate dataset README.md and data_dictionary.csv")
    parser.add_argument("dataset_dir", type=Path, help="Path to the dataset folder (e.g., 02_METADATA or a dataset subfolder)")
    parser.add_argument("--title", default="Dataset Title", help="Dataset title")
    parser.add_argument("--author", default="Your Name", help="Author name")
    parser.add_argument("--description", default="Short description of the dataset.", help="Dataset description")
    parser.add_argument("--methodology", default="How the data were collected (field/lab/model/satellite).", help="Methodology overview")
    parser.add_argument("--qa", default="Validation and cleaning steps performed.", help="Quality assurance summary")
    parser.add_argument("--license", default="CC-BY 4.0", help="License for the dataset")
    parser.add_argument("--contact", default="email@example.org", help="Contact email")

    args = parser.parse_args()

    dataset_dir = args.dataset_dir
    dataset_dir.mkdir(parents=True, exist_ok=True)

    context = {
        "title": args.title,
        "author": args.author,
        "today": date.today().isoformat(),
        "description": args.description,
        "methodology": args.methodology,
        "qa": args.qa,
        "license": args.license,
        "contact": args.contact,
    }

    readme_path = dataset_dir / "README.md"
    dict_path = dataset_dir / "data_dictionary.csv"

    write_readme(readme_path, context)
    write_dictionary(dict_path)

    print(f"Wrote {readme_path}")
    print(f"Ensured {dict_path} exists with headers: {', '.join(DICTIONARY_HEADERS)}")


if __name__ == "__main__":
    main()
