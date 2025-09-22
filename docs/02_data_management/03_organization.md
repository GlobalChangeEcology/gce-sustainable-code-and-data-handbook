# 2.3 Organizing and Naming Data

A fundamental but often neglected aspect of data management is organization. Many projects collapse into chaos simply because files are scattered in ad hoc folders with unclear names.

**Bad practice example:**

```
project/
	data1.csv
	newdata.csv
	final.csv
	final_final.csv
```

**Better practice example:**

```
project/
	data/
		raw/
			survey_responses_2023-04.csv
		processed/
			survey_responses_cleaned.csv
	docs/
		data_dictionary.md
	analysis/
		scripts/
```

Clear folder structures make it obvious which data is raw and which is processed. File naming conventions — for instance, including dates, project codes, or descriptive terms — prevent the dreaded final_final_reallyfinal.csv problem (Borer et al., 2009).
