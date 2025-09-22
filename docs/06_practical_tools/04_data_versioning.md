# 6.4 Data Version Control (DVC) and Git LFS

While Git is excellent for code, it struggles with large binary files such as datasets. Tools like:

- **Git LFS (Large File Storage):** Replaces large files with lightweight pointers in Git.
- **DVC (Data Version Control):** Tracks data files and machine learning models alongside code, enabling reproducible experiments (Kazakova, 2020).

These systems extend the benefits of version control to data-heavy projects, making it possible to reproduce analyses even as datasets evolve.
