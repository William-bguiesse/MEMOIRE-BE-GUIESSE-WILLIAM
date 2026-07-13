import markdown
import json
from abc import ABC, abstractmethod

class Lecteur(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def lire(self):
        pass

# On met en place une classe qui lit le fichier Markdown et le convertit en HTML.
class LecteurMarkdown(Lecteur):
    def lire(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            texte_brut = file.read()

        html_converti = markdown.markdown(texte_brut)
        return html_converti
    
# la fonction lire() lit le fichier Markdown, puis utilise la bibliothèque markdown pour le convertir en HTML. 
# Le résultat est renvoyé sous forme de chaîne de caractères HTML. 
# as file: est utilisé pour s'assurer que le fichier est correctement fermé après sa lecture, même en cas d'erreur.

# On met en place une classe qui lit le fichier JSON et le convertit en dictionnaire Python.
class LecteurJson(Lecteur):
    def lire(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            donnees = json.load(file)

        return donnees