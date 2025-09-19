
# 3. Code Management

## 3.1 Introduction: Code as a Research Output

In modern science, code is no longer just a byproduct of research — it is an essential part of the research record. Scripts, pipelines, and analysis notebooks define how raw data is transformed into results. If this code is lost, undocumented, or poorly structured, the research itself becomes irreproducible (Wilson et al., 2017).

Treating code as a first-class research output, on par with papers and datasets, is therefore a cornerstone of reproducible science.

---

## 3.2 Principles of Good Scientific Code

Scientific code often begins as quick, exploratory scripts. However, without care, such scripts accumulate into a fragile “pile of spaghetti” that only the original author understands.

Key principles for sustainable code include (Wilson et al., 2017):

- **Readability:** Clear, consistent naming and formatting (style guides such as PEP 8 for Python or tidyverse style for R).
- **Modularity:** Break analysis into functions and scripts instead of long monolithic files.
- **Reusability:** Write code that can be adapted or extended.
- **Documentation:** Explain not only what the code does, but also why.

**Example:**

Instead of:

```python
x = [1,2,3,4]; y=[]; 
for i in x: y.append(i*1.2)
```

Better:

```python
def scale_measurements(values, factor=1.2):
	"""Scale input values by a given factor."""
	return [v * factor for v in values]

scaled_data = scale_measurements([1, 2, 3, 4])
```

The second version is easier to understand, reuse, and maintain.

---

## 3.3 Documentation Practices

Documentation is the bridge between code and people. At a minimum, this should include:

- **Inline comments:** Explain tricky steps, but avoid restating the obvious.
- **Docstrings:** Describe function inputs, outputs, and purpose.
- **README files:** Explain the structure of the repository, dependencies, and how to run analyses.
- **Usage examples:** Provide minimal working examples for others to test.

Without documentation, code may run — but it will not communicate.

---

## 3.4 Notebooks vs. Scripts

Interactive notebooks (e.g., Jupyter, RMarkdown) have become central in scientific workflows. They combine code, text, and results in a single document, making them ideal for exploration and communication (Rule et al., 2019).

However, notebooks can also encourage messy practices, such as running cells out of order or mixing exploratory and production code. A good rule of thumb is:

- Use notebooks for exploration and reporting.
- Use scripts and functions for reusable, automated workflows.

---

## 3.5 Version Control with Git

Version control systems track changes in code over time, making it possible to:

- Roll back mistakes.
- Collaborate without overwriting each other’s work.
- Maintain a history of the project.

Git is the most widely used system, with platforms such as GitHub, GitLab, and Bitbucket providing hosting and collaboration features.

Core concepts include:

- **Commits:** Snapshots of changes.
- **Branches:** Parallel lines of development.
- **Merges:** Combining changes.
- **Pull requests:** Proposing and reviewing contributions.

Version control transforms code from a personal artifact into a collaborative, trustworthy record (Ram, 2013).

---

## 3.6 Automation and Workflow Tools

As projects grow, manually running scripts in the right order becomes risky and inefficient. Workflow tools automate pipelines, ensuring analyses are reproducible and portable.

- **Make:** A classic tool for automating workflows.
- **Snakemake (Köster & Rahmann, 2012):** Popular in bioinformatics, inspired by Make but adapted for modern science.
- **Nextflow:** Widely used for large-scale computational pipelines.

These tools capture dependencies between steps, so running `make` or `snakemake` automatically executes tasks in the right order.

---

## 3.7 Testing and Continuous Integration

Errors in code can undermine entire research projects. Software engineering practices like testing are increasingly important in scientific code (Wilson et al., 2017).

- **Unit tests:** Check that individual functions behave as expected.
- **Integration tests:** Verify that multiple components work together.
- **Continuous integration (CI):** Automated services (e.g., GitHub Actions, GitLab CI) run tests whenever code changes are pushed.

Testing increases trust in results and helps prevent silent errors from propagating.

---

## 3.8 Code Sharing and Licensing

Just as with data, sharing code increases transparency and impact. Public repositories on GitHub or institutional servers make it easier for others to reproduce results.

Clear licensing is critical. Without a license, others may legally be unable to reuse your code. Common choices include:

- **MIT License:** Permissive, allows reuse with attribution.
- **GPL (GNU General Public License):** Requires derivative works to remain open-source.
- **Apache 2.0:** Permissive, with explicit patent protection.

Choosing a license communicates how you want your code to be used.

---

## 3.9 Reflection & Exercises

**Reflection:** Open a script you wrote six months ago. Can you immediately understand what it does? If not, what documentation is missing?

**Exercise:** Rewrite one of your scripts into modular functions, adding docstrings.

**Exercise:** Initialize a Git repository for a project, make a few commits, and try branching and merging.

**Discussion prompt:** When is it appropriate to share notebooks, and when should analyses be moved into scripts or packages?

---

## 3.10 Looking Ahead

This chapter has outlined how code can be written, documented, versioned, tested, and shared in ways that support reproducibility and collaboration.

The next chapter will integrate code and data management into reproducible research workflows, focusing on environments, containers, and workflow reproducibility.

---

### ✅ Learning Outcomes Recap

By completing this chapter, you should be able to:

- Write scientific code that is readable, modular, and documented.
- Distinguish between notebooks and scripts and use each appropriately.
- Apply version control with Git for collaboration and history tracking.
- Automate workflows using tools such as Make or Snakemake.
- Understand the role of testing and continuous integration in scientific code.
- Share code responsibly with appropriate licensing.

---

## References

Köster, J., & Rahmann, S. (2012). Snakemake—a scalable bioinformatics workflow engine. Bioinformatics, 28(19), 2520–2522. https://doi.org/10.1093/bioinformatics/bts480

Ram, K. (2013). Git can facilitate greater reproducibility and increased transparency in science. Source Code for Biology and Medicine, 8(1), 7. https://doi.org/10.1186/1751-0473-8-7

Rule, A., Tabard, A., & Hollan, J. D. (2019). Exploration and explanation in computational notebooks. Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems, 32. https://doi.org/10.1145/3173574.3173606

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. PLoS Computational Biology, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510
