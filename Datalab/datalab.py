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
        
        pass