''' Exercice 2
    ¯¯¯¯¯¯¯¯¯¯
    Écrivez une fonction Python qui lit un fichier texte spécifié en paramètre
    et retourne un objet de type liste dont chaque entrée correspond à chaque ligne du fichier.

    Résultat attendu:
        >>> lire_fichier("c:\\scripts\\montypython.txt")
        ['Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Michael Palin']
'''

def lire_fichier(nomfichier):
    with open(nomfichier, 'r') as fichier:
        return [ligne.strip('\n') for ligne in fichier.readlines()]
