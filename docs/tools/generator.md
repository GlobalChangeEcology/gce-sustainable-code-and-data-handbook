# Dataset Docs Generator

The CLI `tools/generate_dataset_docs.py` creates a dataset README and an empty data dictionary CSV for any folder.

## Install
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas
```

## Usage
```bash
python tools/generate_dataset_docs.py --out ./path/to/dataset --name "My Dataset" --owner "Your Lab" --license "CC BY 4.0"
```

Outputs:
- `./path/to/dataset/README.md` — describe purpose, columns, provenance, license
- `./path/to/dataset/data_dictionary.csv` — fill in column metadata

Tip: Commit these files and keep them updated as the dataset evolves.
