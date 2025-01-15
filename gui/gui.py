import tkinter as tk
from tkinter import messagebox
import asyncio

# Simulation de la récolte du Blé (ID 38)
async def collect_wheat():
    # Simuler un délai de récolte de la ressource
    await asyncio.sleep(2)  # Simule un délai de récolte de 2 secondes

    # Logique pour récolter Blé (ID 38)
    # Remplacer cette ligne par la logique réelle de récolte dans ton jeu si nécessaire
    print("Récolte de Blé (ID 38) lancée!")

    # Si la récolte est réussie, retourne un message
    return "Récolte de Blé terminée avec succès!"

# Fonction pour le clic sur le bouton de récolte
async def on_collect_button_click():
    result = await collect_wheat()  # Appelle la fonction de récolte du Blé
    # Affiche un message à l'utilisateur lorsque la récolte est terminée
    messagebox.showinfo("Récolte", result)

# Interface graphique avec Tkinter
def create_gui():
    # Créer la fenêtre principale
    window = tk.Tk()
    window.title("Récolte de Blé")

    # Ajouter un label avec un texte explicatif
    label = tk.Label(window, text="Cliquez sur le bouton pour récolter le Blé!")
    label.pack(pady=10)

    # Ajouter un bouton qui, lorsqu'il est cliqué, lance la récolte
    collect_button = tk.Button(window, text="Récolter le Blé", command=lambda: asyncio.run(on_collect_button_click()))
    collect_button.pack(pady=20)

    # Lancer la fenêtre de l'application
    window.mainloop()

# Lancer l'application graphique lorsque ce fichier est exécuté
if __name__ == "__main__":
    create_gui()
