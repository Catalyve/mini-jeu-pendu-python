import random

HANGMAN = [
    """
     _______
    |/      |
    |
    |
    |
    |
    |
 ___|___
""",
    """
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
 ___|___
""",
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
 ___|___
""",
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |
    |
 ___|___
""",
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |
    |
 ___|___
""",
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      /
    |
 ___|___
""",
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
 ___|___
"""
]


def choisir_mot_depuis_fichier(nom_fichier):
    """Retourne un mot au hasard"""
    with open(nom_fichier, "r", encoding="utf-8") as f:
        lignes = f.read().splitlines()
    return random.choice(lignes)


def afficher_pendu(erreurs):
    """Affiche le dessin en fonction des erreurs."""
    print(HANGMAN[erreurs])

def creer_mot_masque(mot):
    """Crée une liste de '_' du même nombre de lettres que le mot."""
    return ["_"] * len(mot)

def afficher_mot(mot_masque):
    """Affiche le mot avec espaces."""
    print(" ".join(mot_masque))

def demander_lettre():
    """Demande une lettre valide à l'utilisateur."""
    while True:
        lettre = input("Lettre : ").upper()
        if len(lettre) == 1 and lettre.isalpha():
            return lettre
        print("Entre une seule lettre.")

def mettre_a_jour_mot(mot, mot_masque, lettre):
    """
    Remplace les '_' par la lettre si elle est dans le mot.
    Retourne True si la lettre est trouvée, False sinon.
    """
    trouve = False
    for i in range(len(mot)):
        if mot[i] == lettre:
            mot_masque[i] = lettre
            trouve = True
    return trouve

def mot_complet(mot_masque):
    """Retourne True si le mot ne contient plus de '_'."""
    for c in mot_masque:
        if c == "_":
            return False
    return True


def jouer():
    mot = choisir_mot_depuis_fichier("liste_mots")
    mot_masque = creer_mot_masque(mot)
    erreurs = 0
    lettres_tentees = []

    print("=== JEU DU PENDU ===")

    while erreurs < len(HANGMAN) - 1:

        afficher_pendu(erreurs)
        afficher_mot(mot_masque)
        print("Lettres déjà tentées :", " ".join(lettres_tentees))

        lettre = demander_lettre()

        if lettre in lettres_tentees:
            print("Lettre déjà proposée !")
            continue

        lettres_tentees.append(lettre)

        if mettre_a_jour_mot(mot, mot_masque, lettre):
            print("→ Bien vu !")
        else:
            print("→ Mauvais choix.")
            erreurs += 1

        if mot_complet(mot_masque):
            afficher_mot(mot_masque)
            print("🎉 Gagné ! Le mot était", mot)
            return

    afficher_pendu(erreurs)
    print("💀 Pendu ! Le mot était :", mot)

continuer = "o"
while continuer == "o":
    jouer()
    continuer = input("Rejouer 'o'/'n'? ")


print("A bientôt !")

