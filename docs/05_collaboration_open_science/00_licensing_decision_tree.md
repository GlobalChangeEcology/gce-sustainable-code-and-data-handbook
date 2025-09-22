# Licensing Decision Tree

```mermaid
flowchart TD
	A[Do you want to allow any reuse?] -->|No| B[All rights reserved]
	A -->|Yes| C[Require attribution?]
	C -->|No| D[CC0 (public domain)]
	C -->|Yes| E[Allow commercial use?]
	E -->|Yes| F[CC-BY]
	E -->|No| G[CC-BY-NC]
```

For code, consider MIT, GPL, or Apache licenses. For data, CC0 or CC-BY are common.
