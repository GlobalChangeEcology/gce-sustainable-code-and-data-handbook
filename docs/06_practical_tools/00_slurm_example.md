# Using Cloud/HPC Resources (SLURM Example)

If your university provides a cluster, you may use SLURM to submit jobs. Example script:

```bash
#!/bin/bash
#SBATCH --job-name=myjob
#SBATCH --output=output.txt
#SBATCH --ntasks=1
#SBATCH --time=01:00:00
#SBATCH --mem=4G

module load python/3.11
python scripts/example_script.py
```

Submit with: `sbatch myjob.sh`

Check your university’s documentation for details.
