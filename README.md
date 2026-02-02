
# README — Jeu du Pendu (Python)

## Présentation
Ce projet est une implémentation simple du **jeu du pendu en Python**, développée dans un style compréhensible.  
Le joueur doit deviner un mot en proposant des lettres. Chaque erreur affiche progressivement le dessin du pendu.

Le jeu se joue entièrement dans le **terminal**.

---

## Fonctionnalités

- Sélection d’un mot au hasard via un fichier texte  
- Affichage du pendu en ASCII  
- Affichage du mot masqué (_ _ _)  
- Gestion des lettres déjà tentées  
- Détection de victoire ou défaite  
- Code structuré en fonctions simples  
- Compatible Windows / Linux / Mac  

---

## Structure du projet

```
PenduPy/
│── pendu.py
│── liste_mots.txt
└── README.md
```

---

## Lancer le jeu

Dans un terminal, place-toi dans le dossier du projet :

```bash
cd PenduPy
```

Puis lance :

```bash
python pendu.py
```

---

## Format du fichier liste_mots.txt

Le fichier doit contenir **un mot par ligne**, en MAJUSCULES :

```
PYTHON
ALGORITHME
ROBOT
INTERNET
PENDU
...
```

On peut ajouter autant de mots que l'on souhaite.

---

## Explication rapide

- Le programme lit un mot au hasard dans `liste_mots.txt`.  
- Le mot est affiché sous forme de `_`.  
- Le joueur propose des lettres :
  - si la lettre est correcte → elle apparaît dans le mot  
  - sinon → une erreur est ajoutée et le pendu se dessine  
- Le jeu se termine :
  - 🎉 si toutes les lettres sont trouvées  
  - 💀 si le pendu est complet  

---

## Dépendances

Aucune dépendance externe.  
Fonctionne avec **Python 3.x**.

---

## Améliorations possibles

- Mode facile / moyen / difficile  
- Score et statistiques  
- Catégories de mots  
- Couleurs ANSI  
- Mode 2 joueurs 

---

## 📄 Licence
MIT License
