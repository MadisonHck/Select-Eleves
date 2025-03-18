from random import choice
from liste_etudiant.py import liste_des_eleves
# cette fonction a pour but de séléctionner un nom aléatoire dans une liste de nom donner
def selection_aleatoire(liste_eleve):
    choix_aleatoire = choice(liste_eleve)
    
    return choix_aleatoire


