import tkinter as tk
from tkinter import messagebox


def ouvrir_statistiques():
    fen1 = tk.Toplevel()
    fen1.title("statistiques")
    fen1.geometry("300x200")

    label = tk.Label(fen1, text="Bienvenue dans les statistiques", font=("Arial", 12))
    label.pack(pady=40)

def ouvrir_jeux():
    fen2 = tk.Toplevel()
    fen2.title("jeux")
    fen2.geometry("300x200")

    label = tk.Label(fen2, text="Bienvenue dans les jeux", font=("Arial", 12))
    label.pack(pady=40)


root = tk.Tk()
root.title("Interface de Bienvenue")
root.geometry("400x300")


titre = tk.Label(root, text="Bienvenue ", font=("Arial", 16, "bold"))
titre.pack(pady=20)

btn1 = tk.Button(root, text="Accéder aux statistiques", command=ouvrir_statistiques)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Accéder aux jeux", command=ouvrir_jeux)
btn2.pack(pady=10)


root.mainloop()







