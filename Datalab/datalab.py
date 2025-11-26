import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Optional
import logging

#--> plot style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class DataLab:   #<-- Main Class
    '''
    Class that performs data analisys, from overall eval, to health checking and missing values treatments. 
    Each function must have their docstrings available, if you need any extra details
    '''
    def __init__(self, df: pd.DataFrame, df_name: str = "Dataset name"):
        self.df = df
        self.df_name = df_name
        print(f"Initilized DataLab with {self.df_name}")
        
    def health_check(self):
        """
        Performs a basic structural analysis to understand dimensions, types,
        and missingness volume.
        """

        print(f'Performing health check on {self.df_name}')
        rows, cols = self.df.shape

        print(f'Data dimensions:')
        print(f'    Rows: {rows}')
        print(f'    Columns: {cols}')


        duplicated = self.df.duplicated().sum()
        print(f'    Duplicated Rows: {duplicated} | {(duplicated/rows)*100: }')

        null = self.df.isna().sum()
        null_percentage = (self.df.isna().sum()/rows)*100

        missing_values = pd.DataFrame({
            'Missing Values': null,
            'Missing Percentage': null_percentage,
            'Data type': self.df.dtypes
        })

        missing_values = missing_values[missing_values['Missing Values'] > 0].sort_values('Missing Percentage', ascending=False)
        if not missing_values.empty:
            print('\nColumns with missing data:')
            print(missing_values)
            plt.figure(figsize=(10,16))
            sns.heatmap(self.df.isna(), cbar=False, cmap='viridis', yticklabels=False)
            plt.title(label=f'Missing Values - {self.df_name}')
            plt.show()
            
