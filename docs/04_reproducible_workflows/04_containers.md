## 4.4 Containers for Reproducibility

While dependency lists are helpful, they may still fail if underlying system libraries differ. Containers provide a stronger solution by packaging software and dependencies together.

- **Docker:** The most widely used containerization platform in science (Boettiger, 2015).
- **Singularity/Apptainer:** Designed for high-performance computing environments where Docker is not available.

Containers allow researchers to define an environment once and share it with others. A Dockerfile, for example, specifies all software versions needed. Running the container guarantees that the same environment is reproduced elsewhere.

**Example:**
A researcher publishes a bioinformatics pipeline as a Docker image. Others can download and run it without worrying about installing the right tools — ensuring reproducibility across labs.
