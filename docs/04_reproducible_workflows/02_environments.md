## 4.2 The Challenge of Computational Environments

One of the biggest barriers to reproducibility is the computational environment — the combination of software, libraries, operating system, and hardware on which code is run.

A script may work on the author’s laptop but fail on another computer because a package is missing or a version has changed.

Analyses may silently produce different results if underlying algorithms differ across versions of R, Python, or other software.

Documenting and managing environments is therefore a cornerstone of reproducibility.
