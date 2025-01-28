import tkinter as tk
from tkinter import messagebox

def show_content(title, content):
    """Display the selected topic content in a popup."""
    messagebox.showinfo(title, content)

def create_main_window():
    """Create the main application window."""
    topics = [
        ("1. Syntaxe et Types de données", 
        "Python est un langage basé sur l'indentation, ce qui signifie que l'alignement des lignes de code est essentiel pour définir les blocs de code."


        "**Définition des principaux types de données:**\n\n"
        "- **int**: Utilisé pour représenter des nombres entiers."

        "  Exemple: `x = 10`\n"
        "  Exemple supplémentaire: `nombre = -42`\n"
        "- **float**: Utilisé pour représenter des nombres décimaux (nombres à virgule flottante)."

        "  Exemple: `y = 3.14`\n"
        "  Exemple supplémentaire: `pi = 22 / 7`\n"
        "- **str**: Utilisé pour les chaînes de caractères, c'est-à-dire du texte."

        "  Exemple: `texte = 'Bonjour'`\n"
        "  Exemple supplémentaire: `multiligne = '''Bonjour\nMonde'''`\n"
        "- **bool**: Utilisé pour les valeurs booléennes (True ou False)."

        "  Exemple: `is_active = True`\n"
        "  Exemple supplémentaire: `is_even = (x % 2 == 0)`\n"),

        ("2. Structures de contrôle", 
        "Les structures de contrôle permettent de diriger le flux d'exécution du programme en fonction de certaines conditions ou de répéter des actions.\n\n"
        "**Les principales structures de contrôle:**\n\n"
        "- **Conditions**: Elles permettent d'exécuter du code uniquement si une condition est remplie."

        "  Exemple:\n"
        "  ```python\n"
        "  if x > 0:\n"
        "      print('Positif')\n"
        "  elif x == 0:\n"
        "      print('Zéro')\n"
        "  else:\n"
        "      print('Négatif')\n"
        "  ```\n"
        "- **Boucles**: Elles permettent de répéter une ou plusieurs instructions plusieurs fois.\n"
        "  Exemple avec `for`:\n"
        "  ```python\n"
        "  for i in range(5):\n"
        "      print(i)\n"
        "  ```\n"
        "  Exemple avec `while`:\n"
        "  ```python\n"
        "  x = 0\n"
        "  while x < 5:\n"
        "      print(x)\n"
        "      x += 1\n"
        "  ```\n"),

        ("3. Structures de données", 
        "Python propose plusieurs structures pour organiser et manipuler des données.\n\n"
        "**Les principales structures de données en Python:**\n\n"
        "- **Listes**: Collection ordonnée et modifiable d'éléments."
        "  ```python\n"
        "  fruits = ['pomme', 'banane', 'cerise']\n"
        "  fruits.append('orange')\n"
        "  print(fruits)  # ['pomme', 'banane', 'cerise', 'orange']\n"
        "  ```\n"
        "- **Dictionnaires**: Collection non ordonnée d'éléments sous forme clé-valeur."
        "  ```python\n"
        "  personne = {'nom': 'Alice', 'âge': 25}\n"
        "  print(personne['nom'])  # Alice\n"
        "  ```\n"
        "- **Sets et Tuples**:\n"
        "  - **Set**: Collection non ordonnée d'éléments uniques.\n"
        "  ```python\n"
        "  ensemble = {1, 2, 3}\n"
        "  ```\n"
        "  - **Tuple**: Collection ordonnée et immuable.\n"
        "  ```python\n"
        "  tuple_immutable = (1, 2, 3)\n"
        "  ```\n"),

        ("4. Fonctions", 
        "Les fonctions permettent d'organiser votre code en blocs réutilisables.\n\n"
        "**Définition et utilisation des fonctions:**\n\n"
        "- **Définir une fonction**: On utilise le mot-clé `def` suivi du nom de la fonction."
        "  ```python\n"
        "  def saluer(nom):\n"
        "      return f'Bonjour, {nom}!'\n"
        "  print(saluer('Alice'))\n"
        "  ```\n"
        "- **Fonctions Lambda**: Petites fonctions anonymes créées avec le mot-clé `lambda`."
        "  ```python\n"
        "  carré = lambda x: x ** 2\n"
        "  print(carré(4))  # 16\n"
        "  ```\n"),

        ("5. Gestion des erreurs", 
        "Gérez les erreurs pour éviter que votre programme ne plante lors d'entrées invalides ou d'autres problèmes.\n\n"
        "**Exemples de gestion des erreurs:**\n\n"
        "- **Try/Except**: Permet de capturer et de traiter les erreurs."
        "  ```python\n"
        "  try:\n"
        "      x = int(input('Entrez un nombre: '))\n"
        "      print(10 / x)\n"
        "  except ValueError:\n"
        "      print('Ce n\'est pas un nombre valide !')\n"
        "  except ZeroDivisionError:\n"
        "      print('Division par zéro interdite !')\n"
        "  ```\n"),

        ("6. Programmation orientée objet (POO)", 
        "La programmation orientée objet permet de modéliser des entités du monde réel sous forme de classes et d'objets.\n\n"
        "**Concepts de base de la POO en Python:**\n\n"
        "- **Créer une classe**: Une classe est un modèle pour créer des objets."
        "  ```python\n"
        "  class Personne:\n"
        "      def __init__(self, nom, âge):\n"
        "          self.nom = nom\n"
        "          self.âge = âge\n"
        "      def se_presenter(self):\n"
        "          return f'Je m\'appelle {self.nom} et j\'ai {self.âge} ans.'\n"
        "  p = Personne('Alice', 30)\n"
        "  print(p.se_presenter())\n"
        "  ```\n")
    ]

    # Initialiser la fenêtre principale
    window = tk.Tk()
    window.title("Interface de Révision Python")
    window.geometry("700x600")
    window.resizable(width=False, height=False)
    window.configure(bg="#800000")  # Rouge bordeaux

    
    
    # Titre principal
    lbl_title = tk.Label(
        master=window,
        text="Notions Fondamentales de Python",
        font=("Arial", 18, "bold"),
        bg="#800000",
        fg="#FFFFFF",
    )
    lbl_title.pack(pady=10)

    # Variables pour navigation
    current_topic = tk.IntVar(value=0)

    # Affichage des contenus
    def display_topic(index):
        title, content = topics[index]
        lbl_content_title.config(text=title)
        txt_content.delete(1.0, tk.END)
        txt_content.insert(tk.END, content)

    def next_topic():
        if current_topic.get() < len(topics) - 1:
            current_topic.set(current_topic.get() + 1)
            display_topic(current_topic.get())

    def prev_topic():
        if current_topic.get() > 0:
            current_topic.set(current_topic.get() - 1)
            display_topic(current_topic.get())

    # Cadre de contenu principal
    frame_content = tk.Frame(master=window, bg="#800000")
    frame_content.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    lbl_content_title = tk.Label(
        master=frame_content,
        text="",
        font=("Arial", 16, "bold"),
        bg="#800000",
        fg="#FFFFFF",
        anchor="w",
    )
    lbl_content_title.pack(anchor="w", pady=(0, 10))

    txt_content = tk.Text(
        master=frame_content,
                wrap="word",
        font=("Arial", 12),
        bg="#FFFFFF",
        fg="#000000",
        relief=tk.RIDGE,
        height=15,
    )
    txt_content.pack(expand=True, fill=tk.BOTH)

    # Cadre pour les boutons de navigation
    frame_buttons = tk.Frame(master=window, bg="#800000")
    frame_buttons.pack(fill=tk.X, pady=10)

    # Bouton précédent
    btn_prev = tk.Button(
        master=frame_buttons,
        text="⬅ Précédent",
        command=prev_topic,
        bg="#BBDEFB",
        fg="#000000",
        font=("Arial", 12),
        width=15,
    )
    btn_prev.pack(side=tk.LEFT, padx=5)

    # Bouton suivant
    btn_next = tk.Button(
        master=frame_buttons,
        text="Suivant ➡",
        command=next_topic,
        bg="#BBDEFB",
        fg="#000000",
        font=("Arial", 12),
        width=15,
    )
    btn_next.pack(side=tk.LEFT, padx=5)

    # Bouton quitter
    btn_quit = tk.Button(
        master=frame_buttons,
        text="Quitter",
        command=window.destroy,
        bg="#FF6666",
        fg="#FFFFFF",
        font=("Arial", 12),
        width=15,
    )
    btn_quit.pack(side=tk.RIGHT, padx=5)

    # Afficher le premier sujet au lancement
    display_topic(current_topic.get())

    # Lancer l'application
    window.mainloop()


if __name__ == "__main__":
    create_main_window()
