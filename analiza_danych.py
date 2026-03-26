import numpy as np
import matplotlib as mp
import pandas as pd

pd.set_option('display.max_columns', None)

dataset_data_frame = pd.read_csv("SNB_26L_projekt_dane/Diabetes in Pima Indians/pima.tr2", sep=r'\s+')

summary_stats = dataset_data_frame.groupby('type').describe().T

print(summary_stats)