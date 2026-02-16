import csv

class JeuModel:
    def __init__(self, csv_path):
        self.jeux = self._charger_csv(csv_path)

    def _clean_number(self, valeur):
        if not valeur:
            return 0
        return int(valeur.replace(" ", "").replace(" ", ""))  # Nettoyer espaces et espaces insécables

    def _charger_csv(self, path):
        jeux = {}

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                gains = {}
                for key, value in row.items():
                    if key.isdigit() or " " in key:
                        if value:
                            gains[int(key.replace(" ", "").replace(" ", ""))] = self._clean_number(value)

                jeux[row["jeu"]] = {
                    "prix": self._clean_number(row["prix"]),
                    "tickets": self._clean_number(row["unites"]),
                    "gains": gains
                }

        return jeux

    def get_jeu(self, nom):
        return self.jeux.get(nom)

    def calculer_stats(self, jeu):
        mises = jeu["prix"] * jeu["tickets"]
        gains_totaux = sum(g * n for g, n in jeu["gains"].items())
        perte_moyenne = (mises - gains_totaux) / jeu["tickets"] if jeu["tickets"] > 0 else 0
        trj = gains_totaux / mises * 100 if mises > 0 else 0

        return {
            "mises": mises,
            "gains_totaux": gains_totaux,
            "perte_moyenne": perte_moyenne,
            "trj": trj
        }
