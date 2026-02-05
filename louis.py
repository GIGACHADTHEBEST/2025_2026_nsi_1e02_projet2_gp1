import csv
import random
import os

# =========================
# Chargement et nettoyage CSV
# =========================
def to_int(value):
    if value == "" or value is None:
        return 0
    return int(value.replace(" ", "").replace(" ", ""))

def load_data():
    path = os.path.join(os.path.dirname(__file__), "jeux_fdj.csv")
    jeux = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            jeu = {
                "nom": row["jeu"],
                "prix": to_int(row["prix"]),
                "unites": to_int(row["unites"]),
                "total_gains": to_int(row["total_gains"]),
                "gains": {}
            }

            for key, value in row.items():
                if key.isdigit():
                    jeu["gains"][int(key)] = to_int(value)

            jeux.append(jeu)

    return jeux


# =========================
# Simulation d’un ticket
# =========================
def simulate_one(jeu):
    gains_possibles = []

    for gain, count in jeu["gains"].items():
        gains_possibles += [gain] * count

    pertes = jeu["unites"] - len(gains_possibles)
    gains_possibles += [0] * pertes

    gain = random.choice(gains_possibles)
    return gain - jeu["prix"]


# =========================
# Simulation de N tickets
# =========================
def simulate_n(jeu, n):
    results = []
    for _ in range(n):
        results.append(simulate_one(jeu))
    return results


# =========================
# Espérance mathématique
# =========================
def esperance(jeu):
    return (jeu["total_gains"] - jeu["prix"] * jeu["unites"]) / jeu["unites"]


# =========================
# Menu
# =========================
def choose_game(jeux):
    for i, jeu in enumerate(jeux):
        print(f"{i + 1}. {jeu['nom']} ({jeu['prix']} €)")
    index = int(input("Choisissez un jeu : ")) - 1
    return jeux[index]


def menu():
    jeux = load_data()

    while True:
        print("\n=== JEUX D’ARGENT – SIMULATIONS FDJ ===")
        print("1. Simulation d’un ticket")
        print("2. Simulation de plusieurs tickets")
        print("3. Statistiques des jeux")
        print("0. Quitter")

        choice = input("Votre choix : ")

        # -------------------------
        if choice == "1":
            jeu = choose_game(jeux)
            resultat = simulate_one(jeu)

            if resultat >= 0:
                print(f"🎉 Gain : {resultat} €")
            else:
                print(f"❌ Perte : {-resultat} €")

            print(f"📉 Espérance : {esperance(jeu):.2f} €")

        # -------------------------
        elif choice == "2":
            jeu = choose_game(jeux)
            n = int(input("Nombre de tickets à simuler : "))

            results = simulate_n(jeu, n)

            print(f"\n💰 Gain total : {sum(results):.2f} €")
            print(f"📊 Gain moyen : {sum(results)/n:.2f} €")
            print(f"🎯 Tickets gagnants : {sum(1 for r in results if r > 0) / n * 100:.2f} %")

        # -------------------------
        elif choice == "3":
            print("\n📊 ESPÉRANCE PAR JEU")
            jeux_sorted = sorted(jeux, key=esperance, reverse=True)

            for jeu in jeux_sorted:
                print(f"{jeu['nom']:<30} {esperance(jeu):>6.2f} €")

        # -------------------------
        elif choice == "0":
            print("Au revoir 👋")
            break

        else:
            print("Choix invalide.")


# =========================
# Lancement
# =========================
menu()
