# 3) Capture Metadata

Outcomes: dataset README, data dictionary, schema.

Checklist
- [ ] Run the dataset docs generator for each dataset
- [ ] Write `README.md` and `data_dictionary.csv`
- [ ] Add a Frictionless Table Schema and validate

Do it
- `python tools/generate_dataset_docs.py ./02_METADATA/my-dataset`
- `frictionless validate table_schema.json`

Reference
- Metadata & Documentation
- Dataset JSON-LD (optional for web pages)
