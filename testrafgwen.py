import tkinter as tk
import random

PRIX_TICKET = 5

lots = [
    (0, 0.737),
    (5, 0.102),
    (10, 0.119),
    (20, 0.0277),
    (50, 0.0074),
    (100, 0.0074),
    (500, 0.0001),
    (5000, 0.0000004),
    (10000, 0.0000002),
    (100000, 0.0000001),
    (500000, 0.00000016)
]

tickets = 0
argent_net = 0


def ouvrir_statistiques():
    fen1 = tk.Toplevel(root)
    fen1.title("Statistiques")
    fen1.geometry("300x200")

    label = tk.Label(
        fen1,
        text="Bienvenue dans les statistiques",
        font=("Arial", 12)
    )
    label.pack(pady=40)


def ouvrir_jeux():
    global resultat_label, stats_label

    fenetre = tk.Toplevel(root)
    fenetre.title("Ticket à gratter")
    fenetre.geometry("460x360")
    fenetre.resizable(False, False)

    def gratter_ticket():
        r = random.random()
        cumul = 0
        for gain, proba in lots:
            cumul += proba
            if r <= cumul:
                return gain
        return 0

    def gratter_n(n):
        global tickets, argent_net

        gain_total = 0
        depense = n * PRIX_TICKET

        for _ in range(n):
            gain = gratter_ticket()
            gain_total += gain
            argent_net += gain - PRIX_TICKET
            tickets += 1

        argent_depense_total = tickets * PRIX_TICKET

        if n == 1:
            if gain_total == 0:
                resultat_label.config(text="Perdu\n0 €", fg="red")
            else:
                resultat_label.config(text=f"Gagné\n{gain_total} €", fg="green")
        else:
            resultat_label.config(
                text=f"{n} tickets grattés\nGain : {gain_total} €",
                fg="blue"
            )

        if argent_net > 0:
            net_text = f"Argent gagné : {argent_net} €"
            couleur = "green"
        elif argent_net < 0:
            net_text = f"Argent perdu : {-argent_net} €"
            couleur = "red"
        else:
            net_text = "Ni gain ni perte"
            couleur = "black"

        stats_label.config(
            text=(
                f"Tickets grattés : {tickets}\n"
                f"Prix total : {argent_depense_total} €\n"
                f"{net_text}"
            ),
            fg=couleur
        )

    tk.Label(
        fenetre,
        text="JEU DE TICKETS À GRATTER",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    resultat_label = tk.Label(
        fenetre,
        text="Clique pour gratter",
        font=("Arial", 18),
        fg="blue"
    )
    resultat_label.pack(pady=15)

    frame = tk.Frame(fenetre)
    frame.pack(pady=10)

    tk.Button(
        frame,
        text="Gratter 1 ticket (5 €)",
        font=("Arial", 12),
        bg="#FFD700",
        command=lambda: gratter_n(1)
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        frame,
        text="Gratter 100 tickets (500 €)",
        font=("Arial", 12),
        bg="#FFB347",
        command=lambda: gratter_n(100)
    ).grid(row=0, column=1, padx=10)

    stats_label = tk.Label(
        fenetre,
        text=(
            "Tickets grattés : 0\n"
            "Prix total : 0 €\n"
            "Ni gain ni perte"
        ),
        font=("Arial", 12),
        justify="left"
    )
    stats_label.pack(pady=15)


# ===== Fenêtre principale =====
root = tk.Tk()
root.title("Interface de Bienvenue")
root.geometry("400x300")

tk.Label(
    root,
    text="Bienvenue",
    font=("Arial", 16, "bold")
).pack(pady=20)

tk.Button(
    root,
    text="Accéder aux statistiques",
    command=ouvrir_statistiques
).pack(pady=10)

tk.Button(
    root,
    text="Accéder aux jeux",
    command=ouvrir_jeux
).pack(pady=10)

root.mainloop()
