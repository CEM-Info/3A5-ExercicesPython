''' Exercice 4b
    ¯¯¯¯¯¯¯¯¯¯¯
    Faites en sorte que ce script n'accepte pas de valeurs autres que celles de
    1 à 12. Lorsqu'une valeur incorrecte est entrée, un message d'erreur doit
    apparaître, et le script doit redemander à l'utilisateur un choix. Si
    l'utilisateur appuie sur la touche entrée sans rien écrire, le script
    quitte son exécution.

    Résultat attendu:
        Entrez un nombre de 1 à 12: 0
        Le nombre doit être compris entre 1 et 12!
        Entrez un nombre de 1 à 12: 13
        Le nombre doit être compris entre 1 et 12!
        Entrez un nombre de 1 à 12: banane
        Vous devez entrer un nombre!
        Entrez un nombre de 1 à 12: 
        Au revoir!
'''

while True:
    reponse = input("Entrez un nombre de 1 à 12: ")

    # Condition de sortie
    if reponse == "":
        print("Au revoir!")
        exit()

    # Évaluer le nombre
    try:
        nombre = int(reponse)
        if (1 <= nombre <= 12):
            break
        print("Le nombre doit être compris entre 1 et 12!")
    except:
        print("Vous devez entrer un nombre!")
for i in range(1,13):
    print(f"{nombre} x {i} = {nombre * i}")
