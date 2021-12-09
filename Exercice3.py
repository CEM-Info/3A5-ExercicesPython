''' Exercice 3
    ¯¯¯¯¯¯¯¯¯¯
    Écrivez une fonction Python qui retourne le contenu de la variable
    d'environnement USERNAME. Vous aurez besoin du module os (import os).

    Résultat attendu:
        >>> get_username()
        Brian
'''

import os
def get_username():
    return os.environ['USERNAME']
