''' Exercice 1
    ¯¯¯¯¯¯¯¯¯¯
    Écrivez une fonction Python qui prend une liste d'entiers en paramètre et
    retourne la somme de tous ses membres.

    Résultat attendu:
        >>> print(somme_liste([1, 2, 3, 4, 5]))
        15
'''

def somme_liste(liste):
    somme = 0
    for nombre in liste:
        somme += nombre
    return somme
