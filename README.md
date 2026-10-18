# Pumpkin Breaker

Brick breaker sur le thème d'Halloween, codé en Python avec pygame-ce.
Le but est de détruire toutes les briques de la citrouille, mais attention,
la balle s'accélère et vous risquez de perdre le controle..

## Installation

cd weekly_bonus
python -m venv .venv
.venv/bin/pip install -r requirements.txt

## Lancement

.venv/bin/python main.py

## Commandes

- ESPACE : jouer / rejouer
- flèches gauche / droite : déplacer la raquette

## Fonctionnalités

- raquette en dôme : l'angle de renvoi dépend de la zone touchée (7 zones)
- niveau en forme de citrouille
- la balle accélère à chaque brique cassée, ce qui augment le difficulté
- menu, game over et écran de victoire
