import pandas as pd


class JeuxModel:
    def __init__(self, fichier):
        self.df = self._charger_donnees(fichier)
        self.gain_cols = self._nettoyer_donnees()

    def _charger_donnees(self, fichier):
        return pd.read_csv(fichier)

    def _nettoyer_donnees(self):
        df = self.df
        df.columns = df.columns.str.replace(" ", "")

        df.rename(columns={
            "jeu": "nom_jeu",
            "prix": "prix_ticket"
        }, inplace=True)

        for col in df.columns:
            if col != "nom_jeu":
                df[col] = pd.to_numeric(df[col], errors="coerce")

        gain_cols = [
            col for col in df.columns
            if col not in ("nom_jeu", "prix_ticket", "unites", "totalgains")
        ]

        return gain_cols

    def get_prix_disponibles(self):
        return sorted(self.df["prix_ticket"].dropna().unique())

    def get_jeux_par_prix(self, prix):
        if prix == "Tous":
            return sorted(self.df["nom_jeu"].unique())
        return sorted(
            self.df[self.df["prix_ticket"] == float(prix)]["nom_jeu"].unique()
        )

    def get_donnees_jeu(self, jeu, prix):
        if prix == "Tous":
            return self.df[self.df["nom_jeu"] == jeu]
        return self.df[
            (self.df["nom_jeu"] == jeu) &
            (self.df["prix_ticket"] == float(prix))
        ]
