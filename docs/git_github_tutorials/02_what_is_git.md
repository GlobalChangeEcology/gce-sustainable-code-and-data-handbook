# What is Git?

## A Distributed Version Control System

Git is a free and open-source tool designed to help researchers and developers:

- Track changes in their files over time.
- Collaborate with others on the same project.
- Experiment with new ideas without fear of losing progress.

### Key Features of Git

1. **Version History:** Keep a detailed history of every change made to your files.
2. **Branching:** Create separate branches to work on new features or fixes.
3. **Merging:** Combine changes from different branches seamlessly.
4. **Distributed:** Work offline—Git stores the entire repository locally.
5. **Speed:** Perform operations like commits and branching quickly.

Git is the foundation for reproducible, collaborative research coding.

### Visualizing Branches and Merges

```mermaid
gitGraph TB:
	commit id: "version 0.0"
	commit id: "version 0.1"
	checkout main
	branch Steven
	commit id: "new feature"
	commit id: "documentation"
	branch Jane
	checkout Steven
	commit id: "fix code"
	checkout main
	merge Steven
	commit id: "version 0.2"
	checkout Jane
	commit id: "fix documentation"
	checkout main
	merge Jane id: "version 0.4.2"
```