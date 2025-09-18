#!/usr/bin/env nextflow

process SummarizePython {
    conda 'environment.yml'
    input:
    path csv
    output:
    path 'summary_python.csv'
    script:
    """
    python summarize.py
    """
}

workflow {
    csv = file('data/example.csv')
    SummarizePython(csv)
}
