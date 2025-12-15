import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def main():
    # ─────────────────────────────
    # Chargement du CSV
    # ─────────────────────────────
    try:
        df = pd.read_csv("jeux.csv")
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier jeux.csv est introuvable.")
        return

    # Nettoyer noms de colonnes (enlever espaces insécables et espaces)
    df.columns = [col.replace('\u202f', '').replace(' ', '') for col in df.columns]

    # Renommer colonnes pour cohérence (si besoin)
    df = df.rename(columns={"jeu": "nom_jeu", "prix": "prix_ticket"})

    # Nettoyage des colonnes numériques
    for col in df.columns:
        if col != "nom_jeu":
            df[col] = pd.to_numeric(df[col].astype(str).str.replace("\u202f", "").str.replace(" ", ""), errors="coerce")

    # Colonnes à exclure du graphique (non-gains)
    exclude_cols = ["nom_jeu", "prix_ticket", "unites", "totalgains", "gain_max"]

    # Colonnes représentant les gains
    gain_cols = [c for c in df.columns if c not in exclude_cols]

    # Calcul du gain maximum
    df["gain_max"] = df[gain_cols].max(axis=1)

    # ─────────────────────────────
    # Interface graphique
    # ─────────────────────────────
    root = tk.Tk()
    root.title("🎲 Analyse des jeux à gratter - FDJ")
    root.geometry("1200x1000")
    root.configure(bg="#f0f4f7")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Helvetica", 12), background="#f0f4f7")
    style.configure("TButton", font=("Helvetica", 11), padding=6)
    style.configure("TCombobox", font=("Helvetica", 11))

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
        else:
            jeu_var.set("")

    prix_var.trace_add("write", update_jeu_list)

    ttk.Label(frame_filters, text="Prix (€) :").grid(row=0, column=0, padx=10, pady=5)
    prix_menu = ttk.Combobox(frame_filters, textvariable=prix_var, values=prix_list, state="readonly", width=15)
    prix_menu.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame_filters, text="Jeu :").grid(row=0, column=2, padx=10, pady=5)
    jeu_menu = ttk.Combobox(frame_filters, textvariable=jeu_var, state="readonly", width=25)
    jeu_menu.grid(row=0, column=3, padx=10, pady=5)

    update_jeu_list()

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#f0f4f7")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(pady=10)

    stats_label = ttk.Label(root, text="", font=("Helvetica", 12, "bold"), background="#f0f4f7", justify="left")
    stats_label.pack(pady=10)

    def update_graph():
        ax.clear()
        jeu = jeu_var.get()
        prix = prix_var.get()

        if prix == "Tous":
            filtered = df[df["nom_jeu"] == jeu]
        else:
            filtered = df[(df["nom_jeu"] == jeu) & (df["prix_ticket"] == float(prix))]

        if filtered.empty:
            ax.set_title("Aucune donnée disponible pour cette sélection")
            canvas.draw()
            stats_label.config(text="Aucune donnée à afficher.")
            return

        # Transforme les colonnes de gains en format long
        long_gains = filtered[gain_cols].melt(value_name='gain').dropna()

        # Compter combien de tickets donnent chaque montant
        counts = long_gains['gain'].value_counts().sort_index()

        # Graphique horizontal
        ax.barh([f"{int(g):,} €" for g in counts.index], counts.values, color="#2c7ad6", edgecolor="#1c5bbf", height=0.6)
        ax.set_xlabel("Nombre de tickets")
        ax.set_title(f"Répartition des gains pour le jeu : {jeu}", fontsize=16, fontweight='bold')
        ax.invert_yaxis()  # plus gros montant en haut

        # Ajouter valeurs à droite des barres
        for i, (gain, count) in enumerate(zip(counts.index, counts.values)):
            ax.text(count, i, f"{count:,}", va='center', ha='left', fontsize=9)

        plt.tight_layout()

        # Statistiques
        gain_max = int(filtered["gain_max"].max())
        prix_reel = float(prix) if prix != "Tous" else filtered["prix_ticket"].iloc[0]
        prix_txt = f"{prix_reel} €"

        stats_label.config(
            text=f"📌 Statistiques pour « {jeu} »\n➡ Prix du ticket : {prix_txt}\n➡ Gain maximum : {gain_max:,} €\n➡ Nombre total de tickets : {filtered['unites'].sum():,}"
        )

        canvas.draw()



    frame_buttons = tk.Frame(root, bg="#f0f4f7")
    frame_buttons.pack(pady=15)

    ttk.Button(frame_buttons, text="Actualiser", command=update_graph).grid(row=0, column=0, padx=10)
    ttk.Button(frame_buttons, text="Quitter", command=root.destroy).grid(row=0, column=1, padx=10)

    update_graph()
    root.mainloop()

if __name__ == "__main__":
    main()
