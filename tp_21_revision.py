import random

def pair_impair(liste):

    pair = list(filter(lambda x: x % 2 == 0, liste))
    impair = list(filter(lambda x: x % 2 == 1, liste))

    print( "Nombres pairs :", pair)
    print("Nombres impair :", impair)

liste_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Liste d'entiers :", liste_int)
pair_impair(liste_int)

#=================#

def palindromes(liste):

    result = list(filter(lambda x: x == "".join(reversed(x)), liste))

    print("Palindrome(s) :", ", ".join(map(str, result)))

liste_str = ["geeks", "geeg", "keegs", "practice", "aa"]
print("Liste de mots :", liste_str)
palindromes(liste_str)

#=================#

import collections

def anagrammes(liste):

    global mot
    result = list(filter(lambda x: collections.Counter(mot) == collections.Counter(x), liste))

    print("Anagmrme(s) de {} :".format(mot), ", ".join(map(str, result)))

mot = "eegks"
liste_str = ["geeks", "geeg", "keegs", "practice", "aa"]
anagrammes(liste_str)
