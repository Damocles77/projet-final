import tkinter as tk
from tkinter import messagebox

def show_content(title, content):
    """Display the selected topic content in a popup."""
    messagebox.showinfo(title, content)

def create_main_window():
    """Create the main application window."""
    # Detailed content for Python basics
    topics = {
        "Structures de Python": (
            "Les structures de Python permettent d'organiser votre code de manière logique et claire.\n\n"
            "1. Boucles:\n"
            "   - for: Répète une action pour chaque élément d'une liste ou d'une plage.\n"
            "     Exemple: for i in range(5): print(i)\n"
            "   - while: Répète une action tant qu'une condition est vraie.\n"
            "     Exemple: while x < 10: x += 1\n\n"
            "2. Conditions:\n"
            "   - if: Exécute un bloc si une condition est vraie.\n"
            "     Exemple: if x > 0: print('Positif')\n"
            "   - elif: Ajoute une autre condition si la première est fausse.\n"
            "   - else: Exécute un bloc si toutes les conditions précédentes sont fausses.\n"
            "     Exemple: else: print('Négatif')\n\n"
            "3. Fonctions:\n"
            "   - Une fonction regroupe du code réutilisable.\n"
            "     Exemple: def salut(): print('Bonjour!')\n\n"
            "4. Classes:\n"
            "   - Une classe est un plan pour créer des objets.\n"
            "     Exemple: class Personne: def __init__(self, nom): self.nom = nom\n"
        ),
        "Méthodologie": (
            "Pour coder efficacement, suivez ces bonnes pratiques:\n\n"
            "1. Commentaires:\n"
            "   - Utilisez # pour expliquer le code.\n"
            "     Exemple: # Cette fonction calcule la somme.\n\n"
            "2. Bonnes pratiques:\n"
            "   - Donnez des noms explicites aux variables et fonctions.\n"
            "     Exemple: total_facture au lieu de tf.\n"
            "   - Indentez correctement le code (4 espaces par niveau).\n\n"
            "3. Structure du code:\n"
            "   - Organisez votre code en modules et fichiers.\n"
            "   - Exemple: math_utils.py pour regrouper les fonctions mathématiques.\n"
        ),
        "Caractères": (
            "Les caractères sont les bases pour manipuler du texte en Python:\n\n"
            "1. Chaînes:\n"
            "   - Utilisez '' ou \"\" pour définir une chaîne.\n"
            "     Exemple: texte = 'Bonjour'\n\n"
            "2. Échappement:\n"
            "   - Utilisez \n pour un saut de ligne, \t pour une tabulation, \\\ pour un antislash.\n"
            "     Exemple: print('Bonjour\nMonde')\n\n"
            "3. Méthodes courantes:\n"
            "   - .lower(): Convertit en minuscules.\n"
            "   - .upper(): Convertit en majuscules.\n"
            "   - .split(): Divise une chaîne en une liste.\n"
            "     Exemple: 'a,b,c'.split(',') -> ['a', 'b', 'c']\n"
        ),
        "Types d'erreurs": (
            "Les erreurs les plus courantes en Python sont:\n\n"
            "1. SyntaxError:\n"
            "   - Le code a une erreur de syntaxe.\n"
            "     Exemple: if x > 5 print(x) (manque :)\n\n"
            "2. TypeError:\n"
            "   - Une opération est effectuée sur des types incompatibles.\n"
            "     Exemple: '3' + 3 (chaîne + nombre)\n\n"
            "3. ValueError:\n"
            "   - Une fonction reçoit une valeur invalide.\n"
            "     Exemple: int('abc')\n\n"
            "4. IndexError:\n"
            "   - Un index est hors des limites de la liste.\n"
            "     Exemple: liste = [1, 2]; print(liste[3])\n"
        )
    }

    window = tk.Tk()
    window.title("Application de Révision Python")
    window.resizable(width=False, height=False)
    window.configure(bg="#F5F5F5")

    # Create a label for the title
    lbl_title = tk.Label(
        master=window, 
        text="Notions de base de Python", 
        font=("Arial", 16), 
        bg="#F5F5F5", 
        fg="#333333"
    )
    lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

    # Define colors for buttons
    button_colors = ["#FFCDD2", "#BBDEFB", "#C8E6C9", "#FFF9C4"]

    # Create buttons for each topic
    for i, (topic, content) in enumerate(topics.items()):
        btn = tk.Button(
            master=window, 
            text=topic, 
            command=lambda t=topic, c=content: show_content(t, c),
            width=40,
            bg=button_colors[i % len(button_colors)],
            fg="#333333",
            activebackground="#B0BEC5",
            activeforeground="#FFFFFF",
            font=("Arial", 12)
        )
        btn.grid(row=i + 1, column=0, columnspan=2, pady=5)

    # Start the application
    window.mainloop()

if __name__ == "__main__":
    create_main_window()
