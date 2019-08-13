from os import getcwd, chdir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

chdir("data_processing/challenge1/")

df = pd.read_csv("challenge1.csv")

df.head()
