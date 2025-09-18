# Archiving & Fixity

Ensure integrity and longevity of research outputs.

## 3-2-1 rule
- 3 copies, 2 media, 1 offsite

## Checksums & manifests
- Use SHA-256
- Keep a `CHECKSUMS.txt` manifest; verify routinely

```bash
# macOS/Linux
shasum -a 256 file > CHECKSUMS.txt
shasum -a 256 -c CHECKSUMS.txt
```

## BagIt packaging
- Structure data as “bags” with payload and checksums

```bash
pip install bagit
bagit.py --contact-name "Name" my_dataset/
```

## Process
1) Finalize results and metadata
2) Compute/verify checksums
3) Package as BagIt (optional)
4) Deposit in a repository with DOI
5) Retain local/offsite backups and test restores
