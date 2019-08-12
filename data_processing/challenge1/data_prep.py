import numpy as np
import pandas as pd
from os import getcwd

samples = np.arange(-1000,1000).astype(np.float32)
data_dict = {}
for i, j in enumerate(samples):
    data_dict[f"curve 1 at {i}"] = 3*np.sin(j - 2*np.pi)
    data_dict[f"curve 2 at {i}"] = 5*np.exp(j)
    data_dict[f"curve 3 at {i}"] = 10*j**8 + 9*j**7 - 819*j**5 + 4*j**3 - 73*j**2 + 65

df = pd.DataFrame(data_dict, index=[0])
df = df.T
data_path = getcwd() + "/data_processing/challenge1"

df.to_csv(f"{data_path}/challenge1.csv")
