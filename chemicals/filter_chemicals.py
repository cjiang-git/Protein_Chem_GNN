import numpy as np
import pandas as pd

data_path = "/farmshare/user_data/khoang99/cs224w"
chemical_chemical_data = "chemical_chemical.links.detailed.v5.0.tsv"
protein_chemical_data = "9606.protein_chemical.links.detailed.v5.0.tsv"

def load_data(data_path, data_file):
    return pd.read_csv(f"{data_path}/{data_file}", sep="\t")

chemical_chemical = load_data(data_path, chemical_chemical_data)
protein_chemical = load_data(data_path, protein_chemical_data)

chemical_of_interest = list(chemical_chemical["chemical1"].unique()) + list(chemical_chemical["chemical2"].unique()) + list(protein_chemical["chemical"].unique())
chemical_of_interest = list(set(chemical_of_interest))

#write chemical_of_interest to file
with open("chemical_of_interest.txt", "w") as f:
    for item in chemical_of_interest:
        f.write("%s\n" % item)