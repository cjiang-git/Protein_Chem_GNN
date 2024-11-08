export DATA_DIR="/farmshare/user_data/khoang99/cs224w"
wget http://stitch.embl.de/download/chemical_chemical.links.detailed.v5.0.tsv.gz $DATA_DIR/chemical_chemical.links.detailed.v5.0.tsv.gz
wget http://stitch.embl.de/download/protein_chemical.links.detailed.v5.0/9606.protein_chemical.links.detailed.v5.0.tsv.gz $DATA_DIR/chemical_chemical.links.detailed.v5.0.tsv.gz/9606.protein_chemical.links.detailed.v5.0.tsv.gz
wget http://stitch.embl.de/download/chemicals.v5.0.tsv.gz $DATA_DIR/chemicals.v5.0.tsv.gz
gunzip $DATA_DIR/chemical_chemical.links.detailed.v5.0.tsv.gz
gunzip $DATA_DIR/9606.protein_chemical.links.detailed.v5.0.tsv.gz
gunzip $DATA_DIR/chemicals.v5.0.tsv.gz