# test
import pandas as pd
import numpy as np

print("Hello World!")

df = pd.read_csv(
    r"E:\Programmation\data-portfolio\1 - Analyse exploratoire\creditcard.csv"
)

print(df)
print("Max time:", np.max(df["Time"]) / 3600)
