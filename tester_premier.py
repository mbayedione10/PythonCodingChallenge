import random


def tester_premier(nombre: int):
    """Retourner si un nombre est premier ou pas

    Args:
        nombre (int): nombre a verifier

    Returns:
        _type_: True or False
    """
    premier = True
    if nombre == 1:
        premier = False
    else:
        i = 2
        while i < nombre and premier == True:
            if nombre % i == 0:
                premier = False
                i += 1
            else:
                i += 1
    return premier


def afficher_premier(liste: list):
    """Afficher la liste des nombres premiers d'une liste

    Args:
        liste (list): liste des nombres a verifier

    Returns:
        _type_: liste des nombres premiers
    """
    result = []
    for value in liste:
        if tester_premier(value) == True:
            result.append(value)
    return result


if __name__ == '__main__':
    """Create a random list and print "nombres premiers"
    """
    random_list = [random.randint(1, 100) for _ in range(10)]
    print("Random liste: ", random_list)
    result = afficher_premier(random_list)
    print("Liste des nombres premier: ", result)
