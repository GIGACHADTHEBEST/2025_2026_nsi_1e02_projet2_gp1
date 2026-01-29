class JeuxController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self._initialiser_filtres()
        self._connecter_evenements()
        self.update_graph()

    def _initialiser_filtres(self):
        prix_list = ["Tous"] + self.model.get_prix_disponibles()
        self.view.prix_menu["values"] = prix_list
        self.update_jeux()

    def _connecter_evenements(self):
        self.view.prix_var.trace_add("write", lambda *_: self.update_jeux())
        self.view.btn_update.config(command=self.update_graph)

    def update_jeux(self):
        prix = self.view.prix_var.get()
        jeux = self.model.get_jeux_par_prix(prix)

        self.view.jeu_menu["values"] = jeux
        self.view.jeu_var.set(jeux[0] if jeux else "")

    def update_graph(self):
        ax = self.view.ax
        ax.clear()

        jeu = self.view.jeu_var.get()
        prix = self.view.prix_var.get()

        data = self.model.get_donnees_jeu(jeu, prix)

        if data.empty:
            ax.set_title("Aucune donnée")
            self.view.canvas.draw()
            self.view.stats_label.config(text="")
            return

        gains = data[self.model.gain_cols].melt()["value"].dropna()
        counts = gains.value_counts().sort_index()

        ax.barh(counts.index.astype(int).astype(str), counts.values)
        ax.set_xlabel("Nombre de tickets")
        ax.set_title(f"Gains - {jeu}")

        self.view.stats_label.config(text=f"""
Jeu : {jeu}
Prix : {data['prix_ticket'].iloc[0]} €
Gain max : {int(gains.max())} €
Tickets : {int(data['unites'].sum())}
""")

        self.view.canvas.draw()
