# Snakemake Basics — Quick Tutorial

Snakemake lets you define workflows as rules with inputs/outputs.

## Minimal Snakefile
```python
rule all:
	input: "results/summary.txt"

rule summarize:
	input: "data/example.csv"
	output: "results/summary.txt"
	conda: "envs/summarize.yml"
	shell: "python scripts/summarize.py {input} > {output}"
```

## Run locally
```bash
snakemake -c2 --use-conda
```

## Tips
- Use `--cores N` to parallelize
- Put envs under `envs/` and scripts under `scripts/`
- Track outputs in `results/` and avoid writing to inputs
- Use `resources:` for memory/time; profiles for HPC
