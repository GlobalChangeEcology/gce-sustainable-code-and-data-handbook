# DVC/Git LFS: Tracking Large Datasets

**Git LFS:**
```sh
git lfs install
git lfs track "data/large_file.csv"
git add .gitattributes data/large_file.csv
git commit -m "Track large file with Git LFS"
git push
```

**DVC:**
```sh
dvc init
dvc add data/large_file.csv
git add data/large_file.csv.dvc .gitignore .dvc
git commit -m "Track large file with DVC"
git push
dvc push
```
