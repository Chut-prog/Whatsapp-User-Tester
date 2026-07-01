# Got Fuck the 01/07/2026 by the new maj that doesn't permit username changes on PC

# Whatsapp-User-Tester

Whatsapp-User-Tester est un outil d'automatisation conçu pour tester rapidement la disponibilité de pseudos (noms d'utilisateurs) sur WhatsApp. Ce projet utilise l'automatisation de l'interface utilisateur pour interagir avec l'application.

## ⚠️ Avertissement important
Ce projet est **à but purement éducatif**. L'automatisation (botting) peut aller à l'encontre des Conditions d'Utilisation de WhatsApp. L'utilisation de ce script se fait sous votre entière responsabilité.

## Fonctionnalités
* **Automatisation UI :** Utilisation de `pyautogui` pour simuler des interactions clavier et souris.
* **Analyse en temps réel :** Détection de l'état de disponibilité via analyse de pixels.
* **Génération dynamique :** Utilise `itertools` pour générer automatiquement toutes les combinaisons possibles de caractères (lettres + chiffres).
* **Rapport de synthèse :** Affiche un résumé complet à la fin du scan.

## Prérequis
* Python 3.x
* Les bibliothèques suivantes :
    ```bash
    pip install pyautogui pyperclip
    ```

## Utilisation
1. Lancez le script :
   ```bash
   python tester.py
