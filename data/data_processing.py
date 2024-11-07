import pandas as pd
import numpy as np
import torch
import os 
import sys
from Bio import SeqIO
from esm.models.esm3 import ESM3
from esm.sdk.api import ESMProtein, SamplingConfig
from esm.utils.constants.models import ESM3_OPEN_SMALL
from torch_geometric.data import Dataset
from tqdm import tqdm
from huggingface_hub import login
import torch, gc

login()

class StringDB_Dataset(Dataset):
    # esm_model must end in .pt for local model.
    def __init__(self,data_path,fasta_path,esm_model='ESM3_OPEN_SMALL'):
        self.data_path = data_path
        self.fasta_path = fasta_path
        self.esm_model = esm_model
        self.data_cols = self.get_column_names()
        '''
        self.data = self.data.dropna()
        self.data = self.data.reset_index(drop=True)
        self.data = self.data.drop_duplicates()
        self.data = self.data.reset_index(drop=True)
        self.data = self.data.drop(columns=['Unnamed: 0'])
        '''
    
    def get_column_names(self):
        if os.path.exists(self.data_path):
            with open(self.data_path) as f:
                return f.readline().strip().split('\t')
        else:
            Exception('File not found, check filepath')

    
    def get_esm_embeddings(self,out_dir):
        client = ESM3.from_pretrained(self.esm_model)
        with open(self.fasta_path) as handle:
            iter = 0
            for record in tqdm(SeqIO.parse(handle, "fasta")):
                label = record.id
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                output_file = os.path.join(out_dir,f"{label}.pt")
                protein = ESMProtein(sequence=(str(record.seq)))
                protein_tensor = client.encode(protein)
                output = client.forward_and_sample(protein_tensor, SamplingConfig(return_mean_embedding=True))
                result = {"label": record.id, "embeddings": output.mean_embedding}

                gc.collect()
                torch.cuda.empty_cache()
                iter+=1

                torch.save(result,output_file)


    def load_data(self,data_path):
        if os.path.exists(data_path):
            data = pd.read_csv(data_path)
            return data     
