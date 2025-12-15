import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def main():
    # ─────────────────────────────
    # Chargement du CSV
    # ─────────────────────────────
    try:
        df = pd.read_csv("jeux.csv")
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier jeux.csv est introuvable.")
        return

    # ─────────────────────────────
    # Nettoyage et préparation des données
    # ─────────────────────────────
    df = df.rename(columns={"jeu": "nom_jeu", "prix": "prix_ticket"}).dropna(subset=["nom_jeu", "prix_ticket"])
    
    # Nettoyage des colonnes numériques
    for col in df.columns:
        if col != "nom_jeu":
            df[col] = pd.to_numeric(df[col].astype(str).str.replace("\u202f", "").str.replace(" ", ""), errors="coerce")

    # Colonnes représentant les gains
    gain_cols = [c for c in df.columns if c not in ["nom_jeu", "prix_ticket"]]

    # Calcul du gain maximum
    df["gain_max"] = df[gain_cols].max(axis=1)

    # ─────────────────────────────
    # Interface graphique
    # ─────────────────────────────
    root = tk.Tk()
    root.title("🎲 Analyse des jeux à gratter - FDJ")
    root.geometry("1000x700")
    root.configure(bg="#f0f4f7")

    # Styles
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Helvetica", 12), background="#f0f4f7")
    style.configure("TButton", font=("Helvetica", 11), padding=6)
    style.configure("TCombobox", font=("Helvetica", 11))

    # ───────────── Filtres ─────────────
    frame_filters = tk.LabelFrame(root, text="Filtres", padx=15, pady=15, bg="#dce6f0", font=("Helvetica", 12, "bold"))
    frame_filters.pack(fill="x", padx=15, pady=15)

    prix_var = tk.StringVar(value="Tous")
    jeu_var = tk.StringVar()

    prix_list = ["Tous"] + sorted(df["prix_ticket"].dropna().unique().tolist())

    def update_jeu_list(*args):
        if prix_var.get() == "Tous":
            jeux_ok = sorted(df["nom_jeu"].unique())
        else:
            prix_sel = float(prix_var.get())
            jeux_ok = sorted(df[df["prix_ticket"] == prix_sel]["nom_jeu"].unique())
        jeu_menu["values"] = jeux_ok
        if jeux_ok:
            jeu_var.set(jeux_ok[0])

    prix_var.trace_add("write", update_jeu_list)

    ttk.Label(frame_filters, text="Prix (€) :").grid(row=0, column=0, padx=10, pady=5)
    prix_menu = ttk.Combobox(frame_filters, textvariable=prix_var, values=prix_list, state="readonly", width=15)
    prix_menu.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame_filters, text="Jeu :").grid(row=0, column=2, padx=10, pady=5)
    jeu_menu = ttk.Combobox(frame_filters, textvariable=jeu_var, state="readonly", width=25)
    jeu_menu.grid(row=0, column=3, padx=10, pady=5)

    update_jeu_list()

    # ───────────── Graphique ─────────────
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor("#f0f4f7")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(pady=10)

    stats_label = ttk.Label(root, text="", font=("Helvetica", 12, "bold"), background="#f0f4f7", justify="left")
    stats_label.pack(pady=10)

    def update_graph():
        ax.clear()
        jeu = jeu_var.get()
        prix = prix_var.get()

        filtered = df[df["nom_jeu"] == jeu] if prix == "Tous" else df[(df["nom_jeu"] == jeu) & (df["prix_ticket"] == float(prix))]

        if filtered.empty:
            ax.text(0.5, 0.5, "Aucune donnée", ha="center", va="center", fontsize=14)
            stats_label.config(text="Aucune statistique disponible.")
            canvas.draw()
            return

        gain_max = int(filtered["gain_max"].iloc[0])
        ax.bar([jeu], [gain_max], color="#2c7ad6", edgecolor="#1c5bbf")
        ax.set_ylabel("Gain maximum (€)")
        ax.set_title(f"Gain maximum du jeu : {jeu}", fontsize=14)

        prix_txt = "Tous les prix" if prix == "Tous" else f"{prix} €"
        stats_label.config(
            text=f"📌 Statistiques pour « {jeu} »\n➡ Prix du ticket : {prix_txt}\n➡ Gain maximum : {gain_max:,} €"
        )
        canvas.draw()

    # ───────────── Boutons ─────────────
    frame_buttons = tk.Frame(root, bg="#f0f4f7")
    frame_buttons.pack(pady=15)

    ttk.Button(frame_buttons, text="Actualiser", command=update_graph).grid(row=0, column=0, padx=10)
    ttk.Button(frame_buttons, text="Quitter", command=root.destroy).grid(row=0, column=1, padx=10)

    update_graph()
    root.mainloop()

if __name__ == "__main__":
    main()
