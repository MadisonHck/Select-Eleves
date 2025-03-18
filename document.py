from liste_etudiants import liste_des_eleves
from selection_eleve import selection_aleatoire

def generation_plaintext():
    liste_eleves = liste_des_eleves()
    eleve_random = selection_aleatoire(liste_eleves)
    res = "Liste des élèves :\n"

    for eleve in liste_eleves:
        if eleve == eleve_random:
            res += f"* {eleve}\n"
        else:
            res += f"- {eleve}\n"
    
    return res

def generation_html():
    liste_eleves = liste_des_eleves()  # Remets cette ligne une fois les imports disponibles
    eleve_random = selection_aleatoire(liste_eleves)  # Idem pour cette ligne

    html = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Liste des élèves</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            div {
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                padding: 20px;
                width: 300px;
                text-align: center;
            }
            h1 {
                color: #4CAF50;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                padding: 8px;
                margin: 4px 0;
                border-radius: 5px;
                background-color: #e0e0e0;
            }
            .highlight {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Elève selectionné aléatoirement :</h1>
            <ul>
    """

    for eleve in liste_eleves:
        if eleve == eleve_random:
            html += f'<li class="highlight"> {eleve}</li>\n'
        else:
            html += f'<li> {eleve}</li>\n'

    html += """
            </ul>
        </div>
    </body>
    </html>
    """
    return html
