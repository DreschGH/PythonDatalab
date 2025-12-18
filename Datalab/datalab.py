import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Optional
import logging

#--> plot style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
sns.color_palette("tab10")

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
            sns.heatmap(self.df.isna(), cbar=False, yticklabels=False)
            plt.title(label=f'Missing Values - {self.df_name}')
            plt.show()
            
    def explore_distributions(self):
        """
        Plots histograms for numerical data to understand skewness and range.
        """
        print('\n[2] Visualizing numerical data distributions')
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(num_cols) == 0:
            print('\n There are no numerical columns in this dataframe')
            return
        n_cols = 3
        n_rows =(len(num_cols)-1)//n_cols+1
        fig, axes =  plt.subplots(n_rows, n_cols, figsize = (15, 4 * n_rows))
        axes = axes.flatten()

        for i, col in enumerate(num_cols):
            sns.histplot(self.df[col].dropna(), kde=True, ax=axes[i], color='skyblue')
            axes[i].set_title(f'Dist: {col}')
            mean_val = self.df[col].mean()
            median_val = self.df[col].median()
            axes[i].axvline(mean_val, color = 'red', linestyle = '--', label = f'Mean {mean_val:.2f}')
            axes[i].axvline(median_val, color = 'green', linestyle = '--', label = f'Median {median_val:.2f}')
            axes[i].legend()
        
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show() 

if __name__ == "__main__":
    df = pd.read_excel(io=r"C:\Python\125.1\ConciliacaoAR_Nexxera_Extrato\resultadoConciliação.xlsx", engine='openpyxl')
    df = df[['R1BRAD1', 'R2BRAD1', 'R1CITI1', 'R2CITI1', 'R1ITAU3', 'R2ITAU3', 'R2ITAU3', 'R1SANT1', 'R1BBRA1', 'Final']]

    lab = DataLab(df = df, df_name="Conciliação Nexxera")
    lab.health_check()
