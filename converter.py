from jinja2 import Environment, FileSystemLoader
import os

class Converter:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
    
    def rendre_template(self, fichier_name, donnees_contexte):
        template = self.env.get_template(fichier_name)
        html_final = template.render(**donnees_contexte)
        return html_final


"""
Classe Converter :
 -> dir est l'abreviation de directory, il peut donc être interessant de l'utiliser 
pour indiquer que notre variable contient le repertoire (le dossier) de nos fichier md ou json. 
Cela servira pour le package jinja2, qui est utilisé pour le rendu des templates HTML.

 -> template est une variable qui contient "self.env" qui permettait à l'etape 
précédente de charger le dossier contenant les templates HTML. avec get_template, 
on charge le fichier HTML spécifique que l'on souhaite utiliser pour le rendu final.

 -> html_final est une variable qui contient le résultat final du rendu du template HTML 
en remplaçant les emplacements vides par les données que nous avions.
"""

"""
Donc pour le moment, si on résume, on a une classe Converter qui permet : 
 -> de charger le texte brute html qu'on a lu dans l'instance de LecteurMarkdown ou LecteurJson. 
 -> de lui affecter un template HTML en remplaçant les emplacements vides par les données que nous avions.
 -> de renvoyer le résultat final du rendu du template HTML.  
"""

