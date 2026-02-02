import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ================= MESSAGE CONSOLE =================

MESSAGE = """Les jeux d’argent exercent une fascination certaine, nourrie par l’espoir d’un gain rapide et par l’illusion que la chance peut, un jour, tout bouleverser. Pourtant, derrière cette promesse séduisante se cache une réalité bien moins reluisante.

Dans la grande majorité des cas, les jeux d’argent ne profitent pas aux joueurs, mais aux organismes qui les proposent. Les règles sont conçues de manière à garantir des bénéfices aux opérateurs, tandis que les pertes s’accumulent lentement mais sûrement pour les participants. Ce qui commence comme un simple divertissement peut alors devenir une source de frustration, voire de difficultés financières.

De plus, les jeux d’argent comportent un risque réel de dépendance. L’alternance entre espoir et déception peut entraîner un comportement compulsif, poussant certaines personnes à rejouer sans mesure, dans l’espoir de « se refaire ». Cette spirale peut avoir des conséquences lourdes sur la vie personnelle, sociale et professionnelle.

Ainsi, s’il est possible de considérer les jeux d’argent comme un loisir occasionnel, il convient de rester lucide et prudent. Miser de l’argent que l’on ne peut se permettre de perdre n’est jamais une bonne idée. En définitive, les jeux d’argent ne sont pas « ouf » : ils promettent beaucoup, mais offrent bien peu, et rappellent surtout l’importance de la modération et du discernement.
"""


# ================= DONNÉES =================

def charger_donnees(fichier):
    return pd.read_csv(
        fichier,
        sep=",",
        thousands=" ",
        encoding="utf-8"
    )


def nettoyer_donnees(df):
    df.columns = (
        df.columns.str.strip()
        .str.replace(" ", "_")
        .str.lower()
    )

    df = df.rename(columns={
        "jeu": "nom_jeu",
        "prix": "prix_ticket",
        "total_gains": "total_gains"
    })

    for col in df.columns:
        if col != "nom_jeu":
            df[col] = pd.to_numeric(df[col], errors="coerce")

    gain_cols = [
        col for col in df.columns
        if col not in ["nom_jeu", "prix_ticket", "unites", "total_gains"]
    ]

    return df, gain_cols


# ================= INTERFACE =================

def creer_fenetre():
    root = tk.Tk()
    root.title("Analyse des jeux à gratter")
    root.geometry("1000x700")
    return root


def creer_filtres(root, df):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    prix_var = tk.StringVar(value="Tous")
    jeu_var = tk.StringVar()

    prix_list = ["Tous"] + sorted(df["prix_ticket"].dropna().unique().tolist())

    ttk.Label(frame, text="Prix (€)").grid(row=0, column=0, padx=5)
    ttk.Combobox(
        frame, textvariable=prix_var,
        values=prix_list, state="readonly"
    ).grid(row=0, column=1)

    ttk.Label(frame, text="Jeu").grid(row=0, column=2, padx=5)
    jeu_menu = ttk.Combobox(
        frame, textvariable=jeu_var, state="readonly"
    )
    jeu_menu.grid(row=0, column=3)

    return prix_var, jeu_var, jeu_menu


def update_jeux(df, prix_var, jeu_var, jeu_menu):
    if prix_var.get() == "Tous":
        jeux = sorted(df["nom_jeu"].unique())
    else:
        prix_val = float(prix_var.get())
        jeux = sorted(
            df[df["prix_ticket"] == prix_val]["nom_jeu"].unique()
        )

    jeu_menu["values"] = jeux
    if jeux:
        jeu_var.set(jeux[0])


# ================= GRAPHIQUE =================

def creer_graphique(root):
    fig, ax = plt.subplots(figsize=(9, 5))
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack()
    return fig, ax, canvas


def update_graph(df, gain_cols, prix_var, jeu_var, ax, canvas, stats_label):
    ax.clear()

    data = df[df["nom_jeu"] == jeu_var.get()]
    if prix_var.get() != "Tous":
        data = data[data["prix_ticket"] == float(prix_var.get())]

    if data.empty:
        ax.set_title("Aucune donnée")
        canvas.draw()
        stats_label.config(text="")
        return

    gains = data[gain_cols].melt()["value"].dropna()
    counts = gains.value_counts().sort_index()

    ax.barh(counts.index.astype(int).astype(str), counts.values)
    ax.set_xlabel("Nombre de tickets")
    ax.set_title(f"Gains – {jeu_var.get()}")

    stats_label.config(text=f"""
Jeu : {jeu_var.get()}
Prix : {int(data['prix_ticket'].iloc[0])} €
Tickets imprimés : {int(data['unites'].sum()):,}
Gain maximum : {int(gains.max()):,} €
""")

    canvas.draw()


# ================= BOUTONS =================

def creer_boutons(root, callback):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    ttk.Button(frame, text="Actualiser", command=callback)\
        .grid(row=0, column=0, padx=5)

    ttk.Button(frame, text="Quitter", command=root.destroy)\
        .grid(row=0, column=1, padx=5)


# ================= PROGRAMME PRINCIPAL =================

def main():
    print(MESSAGE)   # message UNIQUEMENT dans la console

    df = charger_donnees("jeux.csv")
    df, gain_cols = nettoyer_donnees(df)

    root = creer_fenetre()

    prix_var, jeu_var, jeu_menu = creer_filtres(root, df)

    fig, ax, canvas = creer_graphique(root)

    stats_label = ttk.Label(root, text="", justify="left")
    stats_label.pack(pady=10)

    prix_var.trace_add(
        "write",
        lambda *args: update_jeux(df, prix_var, jeu_var, jeu_menu)
    )

    update_jeux(df, prix_var, jeu_var, jeu_menu)

    creer_boutons(
        root,
        lambda: update_graph(
            df, gain_cols, prix_var, jeu_var, ax, canvas, stats_label
        )
    )

    update_graph(df, gain_cols, prix_var, jeu_var, ax, canvas, stats_label)

    root.mainloop()


if __name__ == "__main__":
    main()
