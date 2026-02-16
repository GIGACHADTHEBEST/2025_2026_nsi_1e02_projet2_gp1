import tkinter as tk
from tkinter import ttk


class StatsView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Répartition réelle des issues")
        self.window.geometry("650x500")
        self.window.resizable(False, False)
        self.window.configure(bg="#1e1e2f")

        # ===== STYLE =====
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Titre.TLabel",
                        background="#1e1e2f",
                        foreground="white",
                        font=("Helvetica", 18, "bold"),
                        anchor="center")

        style.configure("Subtitle.TLabel",
                        background="#1e1e2f",
                        foreground="#cfcfe0",
                        font=("Helvetica", 11),
                        anchor="w")

        style.configure("Retour.TButton",
                        font=("Helvetica", 10),
                        padding=6)

        # ===== FRAME PRINCIPAL =====
        self.main_frame = tk.Frame(self.window, bg="#1e1e2f")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # ===== TITRE =====
        self.label_titre = ttk.Label(
            self.main_frame,
            text="Répartition réelle des issues",
            style="Titre.TLabel"
        )
        self.label_titre.pack(pady=(0, 20))

        # ===== BOUTON RETOUR =====
        self.btn_retour = ttk.Button(
            self.main_frame,
            text=" Retourner au menu",
            style="Retour.TButton",
            command=self.window.destroy
        )
        self.btn_retour.pack(pady=(20, 0))


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = StatsView(root)
    root.mainloop()
