---
title: Biosciences (Biology)
---

# Biosciences Domain Guide

Audience: life sciences and ecology projects collecting omics, imaging, phenotyping, or biodiversity data.

## Quick Checklist

- Pick a community standard early (MIxS, MIAPPE, BIDS, OME‑TIFF, Darwin Core).
- Capture persistent IDs: ORCID, ROR, project IDs; sample/specimen IDs (BioSample/MaterialSample), sequence accessions, DOIs.
- Use machine‑readable metadata templates (ISA‑Tab/ISA‑JSON, MIAPPE TSV/Excel, BIDS JSON/TSV, Darwin Core terms/archives).
- Validate with community tools/portals before deposit (BIDS Validator, ENA/GEO validators, GBIF IPT checks).
- Choose the right repository (discipline first; generalist only if none fits) and ensure license/consent fit.
- Record provenance and quality steps in notebooks/pipelines; export dataset README + data dictionary.

## Standards and Formats

- Omics metadata — MIxS (Genomic Standards Consortium): checklists for metagenomes, genomes, amplicons. Use with BioSample/BioProject where applicable. More: https://gensc.org/mixs/
- Plant phenotyping — MIAPPE: checklist + data model, with templates and mappings to ISA‑Tools and BrAPI. More: https://www.miappe.org/
- Neuroimaging and related — BIDS: folder/files + JSON/TSV metadata; many modality extensions; validator and apps ecosystem. More: https://bids.neuroimaging.io/
- Microscopy — OME‑TIFF/NGFF (OME/Zarr): structured image metadata alongside image data. More: https://www.openmicroscopy.org/
- Biodiversity/ecology — Darwin Core (TDWG): standard terms for occurrences, taxonomy, events; DwC‑A packaging; many extensions (e.g., Humboldt). More: https://www.tdwg.org/standards/dwc/
- Project/package metadata — ISA‑Tab/ISA‑JSON for experimental metadata spanning Investigation–Study–Assay. More: https://isa-tools.org/

## Repositories (Examples)

- Sequencing and omics: ENA/EMBL‑EBI, NCBI GEO, ArrayExpress/BioStudies, PRIDE (proteomics), MetaboLights (metabolomics).
- Biodiversity: GBIF via IPT using Darwin Core; OBIS for marine; national biodiversity portals.
- Imaging: BioImage Archive (via BioStudies), EMPIAR for electron microscopy.
- Generalist (fallback): Zenodo, Figshare — only if a domain repository isn’t suitable.

## Validation and Quality

- Use official validators: BIDS Validator; ENA/GEO submission checks; GBIF IPT data quality & DwC term checks.
- Automate conformance checks in CI (schema validation of JSON/TSV; table schemas; ontology term lookups).
- Capture provenance: run pipelines with explicit inputs/outputs; export citations for software and datasets.

## Ethics & Sensitive Data

- Align consent with intended sharing; anonymise and apply access controls where required. For human genomics, consider controlled‑access archives (e.g., EGA, dbGaP). See Ethics & Consent basics page.

## Pointers and Templates

- FAIRsharing: registry of standards and repositories for biosciences — https://fairsharing.org/
- re3data: global registry of repositories — https://www.re3data.org/
- Darwin Core terms quick reference — https://dwc.tdwg.org/terms/
- BIDS Getting Started + validator — https://bids.neuroimaging.io/
- MIAPPE checklist/templates — https://www.miappe.org/
- ENA submission portal — https://www.ebi.ac.uk/ena
- BioStudies — https://www.ebi.ac.uk/biostudies/
- GEO submission — https://www.ncbi.nlm.nih.gov/geo/

Cross‑links: Basics → Ethics & Consent; Discovery → Dataset JSON‑LD; Data Management → Data Versioning; Guided Project Phases 3, 6, 9.

Last updated: 2025‑09‑18

## Quick‑starts

- BIDS folder skeleton

```bash
project=
mkdir -p "$project"/{sub-01,code,derivatives}
mkdir -p "$project"/sub-01/{anat,func}
cat > "$project"/dataset_description.json <<'JSON'
{
	"Name": "My Study",
	"BIDSVersion": "1.9.0",
	"License": "CC-BY-4.0",
	"Authors": ["Surname, Name"],
	"Acknowledgements": "",
	"Funding": [""],
	"GeneratedBy": [{"Name": "my-pipeline", "Version": "0.1.0"}]
}
JSON
touch "$project"/participants.tsv "$project"/README.md
```

- MIAPPE template link: download the latest Excel/TSV templates from the MIAPPE website templates section and fill Investigation, Study, Germplasm, Environment, Sample, Observed Variables, and Data files consistently. See: https://www.miappe.org/

- Darwin Core Archive (DwC‑A) packaging

```bash
# occurrence.csv (UTF-8) with Darwin Core columns, e.g., occurrenceID,eventDate,scientificName,decimalLatitude,decimalLongitude,basisOfRecord
# meta.xml describes fields and types; eml.xml provides dataset-level metadata.

# Basic structure
dwca_dir=dwca_package
mkdir -p "$dwca_dir"
cp occurrence.csv "$dwca_dir"/
cat > "$dwca_dir"/meta.xml <<'XML'
<archive xmlns="http://rs.tdwg.org/dwc/text/">
	<core encoding="UTF-8" linesTerminatedBy="\n" fieldsTerminatedBy="," fieldsEnclosedBy='"' ignoreHeaderLines="1" rowType="http://rs.tdwg.org/dwc/terms/Occurrence">
		<files><location>occurrence.csv</location></files>
		<id index="0"/>
		<field index="1" term="http://rs.tdwg.org/dwc/terms/eventDate"/>
		<field index="2" term="http://rs.tdwg.org/dwc/terms/scientificName"/>
		<field index="3" term="http://rs.tdwg.org/dwc/terms/decimalLatitude"/>
		<field index="4" term="http://rs.tdwg.org/dwc/terms/decimalLongitude"/>
		<field index="5" term="http://rs.tdwg.org/dwc/terms/basisOfRecord"/>
	</core>
	<metadata>
		<location>eml.xml</location>
	</metadata>
</archive>
XML
zip -r dwca.zip "$dwca_dir"
```
