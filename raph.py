import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt




def load_csv(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        messagebox.showerror("Erreur", f"Fichier introuvable : {filepath}")
        return None


def clean_column_names(df):
    df.columns = [c.replace("\u202f", "").replace(" ", "") for c in df.columns]
    return df


def rename_columns(df):
    return df.rename(columns={"jeu": "nom_jeu", "prix": "prix_ticket"})


def clean_numeric_columns(df):
    for col in df.columns:
        if col != "nom_jeu":
            df[col] = pd.to_numeric(
                df[col].astype(str)
                .str.replace("\u202f", "")
                .str.replace(" ", ""),
                errors="coerce"
            )
    return df


def get_gain_columns(df):
    exclude = ["nom_jeu", "prix_ticket", "unites", "totalgains"]
    return [c for c in df.columns if c not in exclude]


def compute_gain_max(df, gain_cols):
    df["gain_max"] = df[gain_cols].max(axis=1)
    return df


def prepare_dataframe(filepath):
    df = load_csv(filepath)
    if df is None:
        return None, None

    df = clean_column_names(df)
    df = rename_columns(df)
    df = clean_numeric_columns(df)

    gain_cols = get_gain_columns(df)
    df = compute_gain_max(df, gain_cols)

    return df, gain_cols


# ─────────────────────────────────────
# UI
# ─────────────────────────────────────
def create_root():
    root = tk.Tk()
    root.title("Analyse des jeux à gratter - FDJ")
    root.geometry("1200x1000")
    return root


def configure_style():
    ttk.Style()


def create_filter_frame(root):
    frame = tk.LabelFrame(root, text="Filtres", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)
    return frame


def create_prix_variable():
    return tk.StringVar(value="Tous")


def create_jeu_variable():
    return tk.StringVar()


def get_prix_list(df):
    return ["Tous"] + sorted(df["prix_ticket"].dropna().unique().tolist())


def create_prix_menu(frame, prix_var, prix_list):
    ttk.Label(frame, text="Prix (€) :").grid(row=0, column=0, padx=5)
    menu = ttk.Combobox(frame, textvariable=prix_var, values=prix_list, state="readonly")
    menu.grid(row=0, column=1, padx=5)
    return menu


def create_jeu_menu(frame, jeu_var):
    ttk.Label(frame, text="Jeu :").grid(row=0, column=2, padx=5)
    menu = ttk.Combobox(frame, textvariable=jeu_var, state="readonly")
    menu.grid(row=0, column=3, padx=5)
    return menu


def filter_games_by_price(df, prix):
    if prix == "Tous":
        return sorted(df["nom_jeu"].unique())
    return sorted(df[df["prix_ticket"] == float(prix)]["nom_jeu"].unique())


def update_jeu_list(df, prix_var, jeu_var, jeu_menu):
    jeux = filter_games_by_price(df, prix_var.get())
    jeu_menu["values"] = jeux
    jeu_var.set(jeux[0] if jeux else "")


def bind_prix_change(df, prix_var, jeu_var, jeu_menu):
    prix_var.trace_add(
        "write",
        lambda *args: update_jeu_list(df, prix_var, jeu_var, jeu_menu)
    )


def filter_dataframe(df, jeu, prix):
    if prix == "Tous":
        return df[df["nom_jeu"] == jeu]
    return df[(df["nom_jeu"] == jeu) & (df["prix_ticket"] == float(prix))]


def build_gain_distribution(filtered, gain_cols):
    long = filtered[gain_cols].melt(value_name="gain").dropna()
    return long["gain"].value_counts().sort_index()


def create_figure(root):
    fig, ax = plt.subplots(figsize=(10, 5))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(pady=10)
    return fig, ax, canvas


def clear_graph(ax):
    ax.clear()


def draw_bars(ax, counts):
    ax.barh(
        [f"{int(g):,} €" for g in counts.index],
        counts.values
    )
    ax.invert_yaxis()
    ax.set_xlabel("Nombre de tickets")


def annotate_bars(ax, counts):
    for i, count in enumerate(counts.values):
        ax.text(count, i, f"{count:,}", va="center")


def set_graph_title(ax, jeu):
    ax.set_title(f"Répartition des gains – {jeu}")


def refresh_canvas(canvas):
    canvas.draw()


def create_stats_label(root):
    label = ttk.Label(root, text="", justify="left")
    label.pack(pady=10)
    return label


def update_stats(label, filtered, jeu):
    label.config(
        text=(
            f"Jeu : {jeu}\n"
            f"Prix : {filtered['prix_ticket'].iloc[0]} €\n"
            f"Gain max : {int(filtered['gain_max'].max()):,} €\n"
            f"Tickets : {filtered['unites'].sum():,}"
        )
    )


# ─────────────────────────────────────
# MAIN UPDATE
# ─────────────────────────────────────
def update_graph(df, gain_cols, ax, canvas, jeu_var, prix_var, stats_label):
    clear_graph(ax)

    jeu = jeu_var.get()
    prix = prix_var.get()

    filtered = filter_dataframe(df, jeu, prix)

    if filtered.empty:
        ax.set_title("Aucune donnée disponible")
        stats_label.config(text="Aucune donnée")
        refresh_canvas(canvas)
        return

    counts = build_gain_distribution(filtered, gain_cols)

    draw_bars(ax, counts)
    annotate_bars(ax, counts)
    set_graph_title(ax, jeu)
    update_stats(stats_label, filtered, jeu)

    refresh_canvas(canvas)

def create_buttons(root, command_update):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    ttk.Button(frame, text="Actualiser", command=command_update).grid(row=0, column=0, padx=5)
    ttk.Button(frame, text="Quitter", command=root.destroy).grid(row=0, column=1, padx=5)

def main():
    df, gain_cols = prepare_dataframe("jeux.csv")
    if df is None:
        return

    root = create_root()
    configure_style()

    frame_filters = create_filter_frame(root)

    prix_var = create_prix_variable()
    jeu_var = create_jeu_variable()

    prix_list = get_prix_list(df)
    create_prix_menu(frame_filters, prix_var, prix_list)
    jeu_menu = create_jeu_menu(frame_filters, jeu_var)

    bind_prix_change(df, prix_var, jeu_var, jeu_menu)
    update_jeu_list(df, prix_var, jeu_var, jeu_menu)

    _, ax, canvas = create_figure(root)
    stats_label = create_stats_label(root)

    create_buttons(
        root,
        lambda: update_graph(df, gain_cols, ax, canvas, jeu_var, prix_var, stats_label)
    )

    update_graph(df, gain_cols, ax, canvas, jeu_var, prix_var, stats_label)

    root.mainloop()


if __name__ == "__main__":
    main()
 
 