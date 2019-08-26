#!/bin/bash
python wiki_indexer.py $1
mv category doc_titles.txt text title $2
