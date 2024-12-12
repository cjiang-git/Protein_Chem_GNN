#!/bin/bash

# path to storage directory
STORAGE_PATH="/mnt/d/data/"
mkdir -p $STORAGE_PATH

# db paths
STRINGDB_PATH="https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz"
STITCHDB_PATH="http://stitch.embl.de/download/protein_chemical.links.transfer.v5.0.tsv.gz"
STRINGDB_SEQ_PATH="https://stringdb-downloads.org/download/protein.sequences.v12.0.fa.gz"
STITCHDB_SMILE_PATH="http://stitch.embl.de/download/chemicals.v5.0.tsv.gz"

STRINGDB_HU_PATH="https://stringdb-downloads.org/download/protein.physical.links.full.v12.0/9606.protein.physical.links.full.v12.0.txt.gz"
STRINGDB_HU_SEQ_PATH='https://stringdb-downloads.org/download/protein.sequences.v12.0/9606.protein.sequences.v12.0.fa.gz'

: '
# STRING DB
echo "Downloading STRING DB"
wget -nc $STRINGDB_PATH -O "${STORAGE_PATH}stringdb.txt.gz"
gzip -dk "${STORAGE_PATH}stringdb.txt.gz"

echo "Downloading STRING DB SEQUENCES"
wget -nc $STRINGDB_SEQ_PATH -O "${STORAGE_PATH}stringdb_seq.fa.gz"
gzip -dk "${STORAGE_PATH}stringdb_seq.fa.gz"
'

# STRING DB Human
echo "Downloading STRING DB"
wget -nc $STRINGDB_HU_PATH -O "${STORAGE_PATH}stringdb_human.txt.gz"
gzip -dk "${STORAGE_PATH}stringdb_human.txt.gz"

echo "Downloading STRING DB SEQUENCES"
wget -nc $STRINGDB_HU_SEQ_PATH -O "${STORAGE_PATH}stringdb_seq_human.fa.gz"
gzip -dk "${STORAGE_PATH}stringdb_seq_human.fa.gz"

: '
# STITCH DB
#if [ ! -f "${STORAGE_PATH}stitchdb" ]; then
echo "Downloading STITCH DB"
wget -nc $STITCHDB_PATH -O "${STORAGE_PATH}stitchdb.txt.gz"
gzip -dk "${STORAGE_PATH}stitchdb.txt.gz"

echo "Downloading STITCH DB SMILES"
wget -nc $STITCHDB_SMILE_PATH -O "${STORAGE_PATH}stitchdb_smile.tsv.gz"
gzip -dk "${STORAGE_PATH}stitchdb_smile.tsv.gz"
'

