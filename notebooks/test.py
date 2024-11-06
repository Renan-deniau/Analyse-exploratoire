# test
# pip install pandas
# pip install matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Hello World!")

df = pd.read_csv(
    r"E:\Programmation\data-portfolio\1 - Analyse exploratoire\creditcard.csv"
)

print(df)
print("Max time:", np.max(df["Time"]) / 3600)
print("Mean time:", np.mean(df["Time"]) / 3600)


plt.hist(df["Time"], bins=50)
plt.xlabel("Time")
plt.ylabel("Fréquence")
plt.title("Dispersion des valeurs de Time")
plt.show()
