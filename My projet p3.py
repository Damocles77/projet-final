import tkinter as tk
from tkinter import messagebox
import random


class Quiz:
    """Classe principale pour gérer l'application Quiz."""

    def __init__(self):
        # Initialiser les sujets
        self.topics = [
            ("1. Syntaxe et Types de données",
             "Python utilise l'indentation pour structurer le code. Voici les principaux types de données avec des exemples :\n\n"
             "- **int**: Nombres entiers\n"
             "  Exemples :\n"
             "    `x = 10`\n"
             "    `age = 25`\n"
             "    `nombre = -42`\n"
             "- **float**: Nombres décimaux\n"
             "  Exemples :\n"
             "    `pi = 3.14`\n"
             "    `taux = 0.05`\n"
             "    `valeur = 22 / 7`\n"
             "- **str**: Chaînes de caractères\n"
             "  Exemples :\n"
             "    `texte = 'Bonjour'`\n"
             "    `prenom = \"Alice\"`\n"
             "    `multiligne = '''Bonjour\nMonde'''`\n"
             "- **bool**: Booléens (True/False)\n"
             "  Exemples :\n"
             "    `is_active = True`\n"
             "    `is_even = (x % 2 == 0)`\n"
             "    `a_completé = False`\n"),

            ("2. Structures de contrôle",
             "Les structures de contrôle permettent de contrôler le flux logique du programme.\n\n"
             "- **Conditions (`if`, `elif`, `else`)**\n"
             "  Exemples :\n"
             "    ```python\n"
             "    if x > 0:\n"
             "        print('Positif')\n"
             "    elif x == 0:\n"
             "        print('Zéro')\n"
             "    else:\n"
             "        print('Négatif')\n"
             "    ```\n"
             "- **Boucles (`for`, `while`)**\n"
             "  Exemples :\n"
             "    ```python\n"
             "    for i in range(5):\n"
             "        print(i)\n"
             "    ```\n"
             "    ```python\n"
             "    fruits = ['pomme', 'banane', 'cerise']\n"
             "    for fruit in fruits:\n"
             "        print(fruit)\n"
             "    ```\n"
             "    ```python\n"
             "    x = 0\n"
             "    while x < 5:\n"
             "        print(x)\n"
             "        x += 1\n"
             "    ```\n"),

            ("3. Structures de données",
             "Structures de données puissantes :\n\n"
             "- **Listes** : Liste ordonnée et modifiable.\n"
             "  Exemples :\n"
             "    ```python\n"
             "    fruits = ['pomme', 'banane', 'cerise']\n"
             "    fruits.append('orange')\n"
             "    print(fruits)  # ['pomme', 'banane', 'cerise', 'orange']\n"
             "    ```\n"
             "    ```python\n"
             "    nombres = [1, 2, 3, 4]\n"
             "    print(nombres[2])  # 3\n"
             "    ```\n"
             "    ```python\n"
             "    fruits.remove('banane')\n"
             "    print(fruits)  # ['pomme', 'cerise', 'orange']\n"
             "    ```\n"
             "- **Dictionnaires** : Collection clé-valeur.\n"
             "  Exemples :\n"
             "    ```python\n"
             "    personne = {'nom': 'Alice', 'âge': 25}\n"
             "    print(personne['nom'])  # Alice\n"
             "    ```\n"
             "    ```python\n"
             "    personne['ville'] = 'Paris'\n"
             "    print(personne)  # {'nom': 'Alice', 'âge': 25, 'ville': 'Paris'}\n"
             "    ```\n"
             "    ```python\n"
             "    del personne['âge']\n"
             "    print(personne)  # {'nom': 'Alice', 'ville': 'Paris'}\n"
             "    ```\n"
             "- **Sets et Tuples** :\n"
             "  Exemples de Set :\n"
             "    ```python\n"
             "    ensemble = {1, 2, 3, 3}\n"
             "    print(ensemble)  # {1, 2, 3}\n"
             "    ```\n"
             "    ```python\n"
             "    ensemble.add(4)\n"
             "    print(ensemble)  # {1, 2, 3, 4}\n"
             "    ```\n"
             "  Exemples de Tuple :\n"
             "    ```python\n"
             "    tuple_immutable = (1, 2, 3)\n"
             "    print(tuple_immutable[0])  # 1\n"
             "    ```\n"),

            ("4. Fonctions",
             "Les fonctions permettent de structurer le code en regroupant des blocs logiques réutilisables :\n\n"
             "- **Créer une fonction**\n"
             "  Exemples :\n"
             "    ```python\n"
             "    def saluer(nom):\n"
             "        return f'Bonjour, {nom}!'\n"
             "    print(saluer('Alice'))\n"
             "    ```\n"
             "    ```python\n"
             "    def ajouter(a, b):\n"
             "        return a + b\n"
             "    print(ajouter(3, 5))  # 8\n"
             "    ```\n"
             "    ```python\n"
             "    def afficher_message():\n"
             "        print('Ceci est un message.')\n"
             "    afficher_message()\n"
             "    ```\n"),

            ("5. Gestion des erreurs",
             "La gestion des erreurs permet d'éviter les plantages de programme :\n\n"
             "- **Try/Except**\n"
             "  Exemples :\n"
             "    ```python\n"
             "    try:\n"
             "        x = int(input('Entrez un nombre : '))\n"
             "        print(10 / x)\n"
             "    except ValueError:\n"
             "        print('Ce n\'est pas un nombre valide !')\n"
             "    except ZeroDivisionError:\n"
             "        print('Division par zéro interdite !')\n"
             "    ```\n"
             "    ```python\n"
             "    try:\n"
             "        resultat = 5 / 0\n"
             "    except ZeroDivisionError:\n"
             "        print('Erreur : Division par zéro')\n"
             "    ```\n"
             "    ```python\n"
             "    try:\n"
             "        liste = [1, 2, 3]\n"
             "        print(liste[5])\n"
             "    except IndexError:\n"
             "        print('Index hors limite !')\n"
             "    ```\n"),
        ]

        # Questions pour le quiz
        self.quiz_questions = [
            {"question": "Quel type de donnée représente un texte en Python ?", "options": ["str", "int", "float"], "answer": "str"},
            {"question": "Quelle structure est utilisée pour des paires clé-valeur ?", "options": ["Dictionnaire", "Liste", "Tuple"], "answer": "Dictionnaire"},
            {"question": "Quel mot-clé est utilisé pour créer une boucle en Python ?", "options": ["for", "if", "try"], "answer": "for"},
            {"question": "Comment déclare-t-on une fonction en Python ?", "options": ["def", "func", "function"], "answer": "def"},
            {"question": "Comment gère-t-on les erreurs en Python ?", "options": ["try/except", "if/else", "for/while"], "answer": "try/except"}
        ]

        # Variables de quiz
        self.current_quiz_question = 0
        self.score = 0

        # Initialiser l'application GUI
        self.current_topic = 0
        self.window = tk.Tk()
        self.window.title("Quiz Python")
        self.window.geometry("700x600")
        self.window.configure(bg="#800000")

        self.setup_ui()

    def setup_ui(self):
        """Configure les éléments de l'interface utilisateur."""
        lbl_title = tk.Label(
            master=self.window,
            text="Notions Fondamentales de Python",
            font=("Arial", 18, "bold"),
            bg="#800000",
            fg="#FFFFFF"
        )
        lbl_title.pack(pady=10)

        self.frame_content = tk.Frame(master=self.window, bg="#800000")
        self.frame_content.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.lbl_content_title = tk.Label(
            master=self.frame_content,
            text="",
            font=("Arial", 16, "bold"),
            bg="#800000",
            fg="#FFFFFF",
            anchor="w",
        )
        self.lbl_content_title.pack(anchor="w", pady=(0, 10))

        self.txt_content = tk.Text(
            master=self.frame_content,
            wrap="word",
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#000000",
            relief=tk.RIDGE,
            height=15,
        )
        self.txt_content.pack(expand=True, fill=tk.BOTH)

        frame_buttons = tk.Frame(master=self.window, bg="#800000")
        frame_buttons.pack(fill=tk.X, padx=10, pady=10)

        btn_prev = tk.Button(
            master=frame_buttons,
            text="⬅ Précédent",
            command=self.prev_topic,
            bg="#BBDEFB",
            fg="#000000",
            font=("Arial", 12),
            width=15,
        )
        btn_prev.pack(side=tk.LEFT, padx=5)

        btn_next = tk.Button(
            master=frame_buttons,
            text="Suivant ➡",
            command=self.next_topic,
            bg="#BBDEFB",
            fg="#000000",
            font=("Arial", 12),
            width=15,
        )
        btn_next.pack(side=tk.LEFT, padx=5)

        btn_quiz = tk.Button(
            master=frame_buttons,
            text="Commencer le Quiz",
            command=self.start_quiz,
            bg="#4CAF50",
            fg="#FFFFFF",
            font=("Arial", 12),
            width=15,
        )
        btn_quiz.pack(side=tk.LEFT, padx=5)

        btn_quit = tk.Button(
            master=frame_buttons,
            text="Quitter",
            command=self.quit_application,
            bg="#FF6666",
            fg="#FFFFFF",
            font=("Arial", 12),
            width=15,
        )
        btn_quit.pack(side=tk.RIGHT, padx=5)

        self.display_topic(self.current_topic)

    def display_topic(self, index):
        """Affiche le contenu du sujet en fonction de l'index."""
        title, content = self.topics[index]
        self.lbl_content_title.config(text=title)
        self.txt_content.delete(1.0, tk.END)
        self.txt_content.insert(tk.END, content)

    def next_topic(self):
        """Affiche le sujet suivant."""
        if self.current_topic < len(self.topics) - 1:
            self.current_topic += 1
            self.display_topic(self.current_topic)

    def prev_topic(self):
        """Affiche le sujet précédent."""
        if self.current_topic > 0:
            self.current_topic -= 1
            self.display_topic(self.current_topic)

    def start_quiz(self):
        """Démarre le quiz."""
        self.current_quiz_question = 0
        self.score = 0
        random.shuffle(self.quiz_questions)
        for question in self.quiz_questions:
            random.shuffle(question["options"])
        self.show_quiz()

    def show_quiz(self):
        """Affiche une question du quiz."""
        self.frame_content.pack_forget()

        self.quiz_frame = tk.Frame(master=self.window, bg="#800000")
        self.quiz_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        question_data = self.quiz_questions[self.current_quiz_question]
        question = question_data["question"]
        options = question_data["options"]

        lbl_question = tk.Label(
            master=self.quiz_frame,
            text=f"Question {self.current_quiz_question + 1}: {question}",
            font=("Arial", 14, "bold"),
            bg="#800000",
            fg="#FFFFFF",
        )
        lbl_question.pack(pady=10)

        for option in options:
            btn_option = tk.Button(
                master=self.quiz_frame,
                text=option,
                font=("Arial", 12),
                bg="#FFFFFF",
                fg="#000000",
                command=lambda opt=option: self.check_answer(opt)
            )
            btn_option.pack(fill=tk.X, pady=5)

    def check_answer(self, selected_option):
        """Vérifie si la réponse est correcte et passe à la question suivante."""
        correct_answer = self.quiz_questions[self.current_quiz_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1

        self.current_quiz_question += 1

        if self.current_quiz_question < len(self.quiz_questions):
            self.quiz_frame.destroy()
            self.show_quiz()
        else:
            self.show_score()

    def show_score(self):
        """Affiche le score final et permet de relancer le quiz ou de quitter."""
        self.quiz_frame.destroy()
        messagebox.showinfo("Quiz terminé", f"Votre score est {self.score} sur {len(self.quiz_questions)}.")
        self.frame_content.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def quit_application(self):
        """Ferme l'application."""
        self.window.destroy()


def start_quiz_app():
    """Instancie la classe Quiz et exécute la boucle principale."""
    app = Quiz()
    app.window.mainloop()


if __name__ == "__main__":
    start_quiz_app() 