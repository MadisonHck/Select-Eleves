# Tirage aléatoire d'un élève avec affichage web

Ce projet permet de gérer une liste d'élèves, de sélectionner un élève au hasard, et d'afficher les résultats via une interface web en utilisant Bottle.

## 📁 Structure du projet

- `liste_etudiants.py` : Contient la liste des élèves.
- `selection_eleve.py` : Sélectionne un élève au hasard à partir du fichier précédent.
- `document.py` : Génère un affichage basé sur les données de `liste_etudiants.py` et `selection_eleve.py`.
- `serveur_web.py` : Héberge une interface web avec Bottle pour afficher les résultats à partir du fichier précédent.

## 🚀 Installation et utilisation

### Prérequis
- Python 3.x installé
- Bibliothèque Bottle installée :  
  ```bash
  pip install bottle
