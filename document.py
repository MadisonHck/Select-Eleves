from liste_etudiants import liste_des_eleves
from selection_eleve import selection_aleatoire

def generation_plaintext():
    liste_eleves = liste_des_eleves()
    eleve_random = selection_aleatoire(liste_eleves)
    res = ''
    
    for eleve in liste_eleves:
        if eleve == eleve_random :
            res += '*' + eleve + '\n'
        else :
            res += "-" + eleve + '\n'

    return res
