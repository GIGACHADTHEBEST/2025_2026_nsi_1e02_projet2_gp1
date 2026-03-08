from view.jeu_view import JeuView
import random


class JeuController:
    def __init__(self, root, catalogue):
        self.catalogue = catalogue
        self.view = JeuView(root)

        jeux_noms = [jeu.nom for jeu in catalogue.jeux]
        self.view.combo_jeu["values"] = jeux_noms

        self.view.btn_jouer.config(command=self.jouer)
        self.canvas = self.view.canvas_visualisation


    def jouer(self):
        nom_jeu = self.view.combo_jeu.get()
        if not nom_jeu:
            return

        jeu = self.catalogue.get_jeu(nom_jeu)
        gain = jeu.tirage_aleatoire()

        if gain > 0:
            self.view.label_resultat.config(
                text=f"Vous avez gagné {gain} € \n Même lorsqu'on croit gagner, on perd sur le long terme."
            )
        else:
            self.view.label_resultat.config(
                text="Ticket perdant \n Vous récupérez très peu de l'argent dépensé.\n"
                 "Les jeux d'argent sont conçus pour faire perdre."
            )
        
        
        

        

