# Conda Environments — Quick Tutorial

Learn to create, reproduce, and share Conda environments.

## Create an environment
```bash
conda create -n gce-handbook python=3.11
conda activate gce-handbook
pip install -r requirements.txt  # or: conda install pandas numpy
```

## Export for sharing
```bash
conda env export --from-history > environment.yml
```

Tip: `--from-history` avoids pinning every transient dependency; for exact reproducibility, consider `conda-lock`.

## Faster solves
```bash
# optional but faster
conda install -n base conda-forge::mamba
mamba env create -f environment.yml
```

## Use in Snakemake
```bash
snakemake -c2 --use-conda
# In rules, set: conda: "envs/myrule.yml"
```

## Use in Nextflow
```bash
nextflow run main.nf -with-conda environment.yml
```

## Good practices
- Keep `environment.yml` at repo root or under `envs/`
- Prefer channels: `conda-forge` first
- Pin major versions; avoid over-pinning micro versions
