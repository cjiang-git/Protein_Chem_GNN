import pandas as pd
import numpy as np
import os 
import sys

class DataProcessing(object):
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(data_path)
        self.data = self.data.dropna()
        self.data = self.data.reset_index(drop=True)
        self.data = self.data.drop_duplicates()
        self.data = self.data.reset_index(drop=True)
        self.data = self.data.drop(columns=['Unnamed: 0'])
    
    
    def load_data(self,data_path):
        if os.path.exists(data_path):
            data = pd.read_csv(data_path)
            return data
                                            
