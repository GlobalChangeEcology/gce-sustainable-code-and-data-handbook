# Data Versioning at Scale

When datasets exceed Git’s comfort zone (size or churn), layer a data versioning system.

## Options
- Git LFS: simple pointer-based tracking; good for medium binaries.
- DVC: versions data/models in S3/SSH/local remotes; pipelines; reproducibility.
- DataLad (git-annex): decentralised, robust for large/heterogeneous datasets.

## DVC quick start
```bash
pip install dvc[dvcs]
dvc init
# configure remote (e.g., S3 or local)
dvc remote add -d data s3://my-bucket/path
# track data
dvc add data/raw/
# commit pointer files and push data
git add data/raw.dvc .gitignore
git commit -m "Track raw data with DVC"
dvc push
```

## DataLad quick start
```bash
pip install datalad
# create dataset
datalad create my-dataset
cd my-dataset
# add data (managed by git-annex)
datalad save -m "Add data" data/
# add a sibling (remote)
datalad create-sibling-github my-dataset --access-protocol ssh
```

## Pros and cons
- LFS: +simple; -storage quotas on Git hosts
- DVC: +pipelines & caching; -requires remote backend setup
- DataLad: +decentralised & powerful; -steeper learning curve

## Recommendations
- Start with Git LFS for small/medium binaries.
- Use DVC when teams need remotes and pipelines.
- Consider DataLad for very large or distributed research datasets.
