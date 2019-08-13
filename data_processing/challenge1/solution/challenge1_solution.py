from os import getcwd, chdir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

chdir("data_processing/challenge1/")

df = pd.read_csv("challenge1.csv")

df.head()


def process(df):
    df.columns = ["Curves", "Values"]

    curve_df = pd.DataFrame()
    curve_df['curve 1'] = df[df['Curves'].str.startswith("curve 1")]['Values'].reset_index(drop=True)
    curve_df['curve 2'] = df[df['Curves'].str.startswith("curve 2")]['Values'].reset_index(drop=True)
    curve_df['curve 3'] = df[df['Curves'].str.startswith("curve 3")]['Values'].reset_index(drop=True)

    return curve_df


processed_df = process(df)

processed_df.head()

# Plot

from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)

x = np.arange(-1000, 1000)

fig, ((ax1, ax2, ax3)) = plt.subplots(1,3, figsize=(30,15))
ax1.scatter(x, processed_df['curve 1'])
ax1.set_xlabel("Values", size=20, color="silver")
ax1.set_ylabel("Curve 1 Function", size=16, color="silver")
ax2.scatter(x, processed_df['curve 2'])
ax2.set_xlabel("Values", size=20, color="silver")
ax2.set_ylabel("Curve 2 Function", size=20, color="silver")
ax3.scatter(x, processed_df['curve 3'])
ax3.set_xlabel("Values", size=20, color="silver")
ax3.set_ylabel("Curve 3 Function", size=20, color="silver")
plt.suptitle("Scatter Plots from Curve Data Frame", size=30, color="gold")
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("solution/curve_df_plot.png")
