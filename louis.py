import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Jeux d'argent – simulations et statistiques",
    layout="wide"
)

# ---------------------------
# Chargement et nettoyage CSV
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("jeux_fdj.csv")

    # Nettoyage des colonnes numériques
    for col in df.columns[1:]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(" ", "", regex=False)
            .str.replace(" ", "", regex=False)
            .replace("", np.nan)
            .astype(float)
        )

    return df


df = load_data()

# Colonnes correspondant aux gains possibles
gain_cols = df.columns[4:]

# ---------------------------
# Fonctions utiles
# ---------------------------
def simulate_ticket(row):
    """Simule un ticket unique"""
    prix = row["prix"]
    total_units = row["unites"]

    gains = []
    for g in gain_cols:
        count = row[g]
        if not np.isnan(count) and count > 0:
            gains += [float(g)] * int(count)

    # Perdant
    losing = int(total_units - len(gains))
    gains += [0] * losing

    result = np.random.choice(gains)
    return result - prix


def simulate_n_tickets(row, n):
    return [simulate_ticket(row) for _ in range(n)]


# ===========================
# PAGE D’ACCUEIL
# ===========================
st.title("🎰 Jeux d’argent : quelles sont vraiment vos chances de gagner ?")

st.markdown(
    """
Les jeux à gratter promettent souvent des gains attractifs…  
**mais se valent-ils réellement ?**

À partir des **données officielles de la Française des Jeux**,  
nous avons analysé les principaux tickets disponibles afin de mieux comprendre :

- vos **probabilités de gain**
- les **montants espérés**
- les **différences entre les jeux**

👉 Les chances de gagner sont **strictement identiques** à celles du commerce.

**Simuler pour mieux comprendre** :  
vous pouvez lancer des simulations pour observer le hasard sur le long terme.
"""
)

st.divider()

# ===========================
# ONGLETS
# ===========================
tab1, tab2, tab3 = st.tabs(
    ["🎲 Simulation simple", "🔁 Simulation 10 000 tickets", "📊 Statistiques"]
)

# ===========================
# ONGLET 1 — SIMULATION SIMPLE
# ===========================
with tab1:
    st.header("🎲 Simulation d’un ticket")

    jeu = st.selectbox("Choisissez un jeu :", df["jeu"])
    row = df[df["jeu"] == jeu].iloc[0]

    if st.button("Gratter un ticket 🎟️"):
        gain = simulate_ticket(row)

        if gain >= 0:
            st.success(f"🎉 Gain : {gain:.2f} €")
        else:
            st.error(f"❌ Perte : {abs(gain):.2f} €")

        esperance = (row["total_gains"] - row["prix"] * row["unites"]) / row["unites"]
        st.info(f"📉 Espérance mathématique par ticket : {esperance:.2f} €")


# ===========================
# ONGLET 2 — SIMULATION MASSIVE
# ===========================
with tab2:
    st.header("🔁 Simulation de plusieurs tickets")

    jeu2 = st.selectbox("Choisissez un jeu :", df["jeu"], key="jeu2")
    row2 = df[df["jeu"] == jeu2].iloc[0]

    n = st.slider("Nombre de tickets simulés", 100, 100000, 10000, step=100)

    if st.button("Lancer la simulation 🚀"):
        results = simulate_n_tickets(row2, n)
        results = np.array(results)

        st.metric("💰 Gain total", f"{results.sum():.2f} €")
        st.metric("📊 Gain moyen", f"{results.mean():.2f} €")
        st.metric("📉 % de tickets gagnants", f"{(results > 0).mean() * 100:.2f} %")

        fig, ax = plt.subplots()
        ax.plot(np.cumsum(results))
        ax.set_title("Évolution du solde")
        ax.set_xlabel("Nombre de tickets")
        ax.set_ylabel("Solde (€)")
        st.pyplot(fig)


# ===========================
# ONGLET 3 — STATISTIQUES
# ===========================
with tab3:
    st.header("📊 Comparaison des jeux")

    stats = []

    for _, row in df.iterrows():
        esperance = (row["total_gains"] - row["prix"] * row["unites"]) / row["unites"]
        stats.append({
            "Jeu": row["jeu"],
            "Prix (€)": row["prix"],
            "Espérance (€)": esperance
        })

    stats_df = pd.DataFrame(stats).sort_values("Espérance (€)", ascending=False)

    st.dataframe(stats_df, use_container_width=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(stats_df["Jeu"], stats_df["Espérance (€)"])
    ax.axvline(0, color="red", linestyle="--")
    ax.set_title("Espérance mathématique par jeu")
    st.pyplot(fig)
