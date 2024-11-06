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
print("Max amount:", np.max(df["Amount"]))
print("Mean amount:", np.mean(df["Amount"]))

# Checking de l'allure de Time
plt.hist(df["Time"], bins=50)
plt.xlabel("Time")
plt.ylabel("Fréquence")
plt.title("Dispersion des valeurs de Time")
plt.show()

# Checking de l'allure de Amount
plt.hist(df["Amount"], bins=50)
plt.xlabel("Amount")
plt.ylabel("Fréquence")
plt.title("Dispersion des valeurs de Amount")
plt.show()


def afficher_deciles(df):
    deciles = df["Amount"].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    deciles = deciles.to_frame("Déciles")
    deciles["Valeur"] = deciles.index * 1

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.table(
        cellText=deciles.values,
        colLabels=deciles.columns,
        loc="center",
        cellLoc="center",
    )
    ax.axis("off")
    plt.title("Déciles de la variable Amount")
    plt.show()


afficher_deciles(df)

print(df["Class"].unique())
print(df["Class"].value_counts())


def afficher_graphique(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["Time"], df["Amount"])
    plt.xlabel("Time")
    plt.ylabel("Amount")
    plt.title("Évolution de l'Amount en fonction du Time")
    plt.grid(True)
    plt.show()


afficher_graphique(df)
