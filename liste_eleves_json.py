import json

with open("eleves.json", "r", encoding="utf-8") as file:
    eleves = json.load(file)

def select_eleve_json():
    noms = []  
    for eleve in eleves:
        noms.append(eleve['nom'])  
    return noms  



