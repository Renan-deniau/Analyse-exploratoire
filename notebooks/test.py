# test
# pip install pandas
# pip install matplotlib
# pour activer le venv .venv\Scripts\activate

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
plt.fill_between(
    [
        df["Amount"].mean() - df["Amount"].std(),
        df["Amount"].mean() + df["Amount"].std(),
    ],
    [0, 100000],
    alpha=0.2,
    label="Écart type",
)
plt.xlabel("Amount")
plt.ylabel("Fréquence")
plt.title("Dispersion des valeurs de Amount")
plt.show()

# Checking de l'allure de Amount zoom
plt.hist(df["Amount"], bins=150, range=[0, 200])
plt.axvline(df["Amount"].median(), color="red", linestyle="--", label="Médiane")
plt.xlabel("Amount")
plt.ylabel("Fréquence")
plt.title("Dispersion des valeurs de Amount")
plt.legend()
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

# Histogramme de la colonne Time
plt.figure(figsize=(12, 6))
plt.hist(df["Time"], bins=50, color="teal")
plt.title(
    "Nombre de secondes écoulées entre cette transaction et la première transaction dans le dataset"
)
plt.xlabel("Secondes")
plt.ylabel("Nombre de transactions")
# Statistiques de base
time_stats = df["Time"].describe()
print("Statistiques de la colonne Time :")
print(time_stats)
# Affichage du graphique
plt.show()

import matplotlib.ticker as ticker


# Définition du format des axes
def format_axis(x, pos):
    if x >= 1000:
        return f"{x/1000:.3g}k"
    elif x >= 1000000:
        return f"{x/1000000:.3g}M"
    else:
        return f"{x:.3g}"


def afficher_variable(df, colonne):
    # Histogramme de la colonne Time
    fig, axs = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={"width_ratios": [5, 2]})

    # Histogramme
    axs[0].hist(df[colonne], bins=50, color="cornflowerblue")
    axs[0].set_title(
        f"Histogramme de la variable {colonne}", fontsize=14, fontweight="bold"
    )
    axs[0].set_xlabel("Secondes")
    axs[0].set_ylabel("Nombre de transactions")

    # Application du format aux axes
    axs[0].xaxis.set_major_formatter(ticker.FuncFormatter(format_axis))
    axs[0].yaxis.set_major_formatter(ticker.FuncFormatter(format_axis))

    # Calcul des statistiques
    time_stats = df[colonne].describe()

    # Affichage des statistiques sur le graphique avec trois chiffres significatifs
    stats_text = (
        f"Count: {int(time_stats['count'])}\n"
        f"Mean: {format_axis(time_stats['mean'], 0)}\n"
        f"Std Dev: {format_axis(time_stats['std'], 0)}\n"
        f"Min: {format_axis(time_stats['min'], 0)}\n"
        f"25%: {format_axis(time_stats['25%'], 0)}\n"
        f"50% (Median): {format_axis(time_stats['50%'], 0)}\n"
        f"75%: {format_axis(time_stats['75%'], 0)}\n"
        f"Max: {format_axis(time_stats['max'], 0)}"
    )

    # Créer deux colonnes de texte dans la boîte à droite du graphique
    bbox = dict(facecolor="white", alpha=0.5, boxstyle="square", ec="black")
    x1 = 0.1
    y1 = 0.8
    x2 = x1 + 0.8
    axs[1].axis("off")  # Supprimer les axes
    axs[1].text(
        x1,
        y1,
        "Statistique",
        transform=axs[1].transAxes,
        fontsize=10,
        ha="left",
        va="center",
        bbox=bbox,
    )
    axs[1].text(
        x2,
        y1,
        "Valeur",
        transform=axs[1].transAxes,
        fontsize=10,
        ha="right",
        va="center",
        bbox=bbox,
    )

    # Afficher les statistiques dans les deux colonnes
    y2 = y1 - 0.1
    for stat in stats_text.split("\n"):
        label, value = stat.split(":")
        axs[1].text(
            x1,
            y2,
            label,
            transform=axs[1].transAxes,
            fontsize=10,
            ha="left",
            va="center",
        )
        axs[1].text(
            x2,
            y2,
            value,
            transform=axs[1].transAxes,
            fontsize=10,
            ha="right",
            va="center",
        )
        y2 -= 0.05

    # Affichage du graphique
    plt.tight_layout()
    plt.show()


afficher_variable(df, "Time")

# for colonne in df.columns:
#   afficher_variable(df,colonne)
