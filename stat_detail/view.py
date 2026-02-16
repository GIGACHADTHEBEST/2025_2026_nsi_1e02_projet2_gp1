import tkinter as tk
from math import ceil

class StatsView:
    def __init__(self, root):
        self.root = root

    def afficher(self, nom_jeu, jeu, stats):
        stats_win = tk.Toplevel(self.root)
        stats_win.title(f"Statistiques – {nom_jeu}")
        stats_win.geometry("1350x880")

        canvas = tk.Canvas(stats_win, bg="white")
        canvas.pack(fill="both", expand=True)

        canvas.create_text(
            675, 30,
            text=f"{nom_jeu} – répartition réelle des issues",
            font=("Arial", 18, "bold")
        )

        x0, y0 = 40, 85
        index = 0
        stats_y = 70
        couleur_index = 0

        canvas.create_text(
            850, 55,
            text="Statistiques détaillées",
            font=("Arial", 16, "bold"),
            anchor="w"
        )

        for gain, nb_tickets in sorted(jeu["gains"].items()):
            couleur = COULEURS[couleur_index % len(COULEURS)]
            couleur_index += 1

            nb_carres = ceil(nb_tickets / CARRE_PAR_TICKETS)
            proba = nb_tickets / jeu["tickets"] * 100
            gain_total = gain * nb_tickets

            for _ in range(nb_carres):
                cx = x0 + (index % PAR_LIGNE) * (TAILLE + MARGE)
                cy = y0 + (index // PAR_LIGNE) * (TAILLE + MARGE)
                canvas.create_rectangle(cx, cy, cx + TAILLE, cy + TAILLE,
                                        fill=couleur, outline="")
                index += 1

            canvas.create_rectangle(820, stats_y - 10, 845, stats_y + 10,
                                    fill=couleur, outline="")

            canvas.create_text(
                855, stats_y,
                text=(f"Gain {gain} €\n"
                      f"{nb_tickets:,} tickets • {proba:.4f} %\n"
                      f"Gains totaux : {gain_total:,} €").replace(",", " "),
                anchor="w", font=("Arial", 11)
            )

            stats_y += 65

        canvas.create_text(
            855, stats_y + 20,
            text=(f"Prix du ticket : {jeu['prix']} €\n"
                  f"Mise totale : {stats['mises']:,} €\n"
                  f"Gains redistribués : {stats['gains_totaux']:,} €\n"
                  f"Taux de redistribution : {stats['trj']:.2f} %\n"
                  f"Perte moyenne par ticket : {stats['perte_moyenne']:.2f} €").replace(",", " "),
            anchor="w", font=("Arial", 12, "bold"),
            fill="darkred"
        )

        tk.Button(stats_win, text="⬅ Retour au menu",
                  font=("Arial", 12),
                  command=stats_win.destroy).pack(pady=15)


if __name__ == "__main__":
    root = tk.Tk()
    app = StatsView(root)
    root.mainloop()
