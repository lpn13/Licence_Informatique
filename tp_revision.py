#====================================================#
import random

def rand_list(n):
    return random.sample(range(-10, 10), n)

# print("Liste aléatoire :", rand_list(10))

#====================================================#

def pair_impair(list1, list2):

    pair1 = list(filter(lambda x: x % 2 == 0, list1))
    pair2 = list(filter(lambda x: x % 2 == 0, list2))
    
    impair1 = list(filter(lambda x: x % 2 == 1, list1))
    impair2 = list(filter(lambda x: x % 2 == 1, list2))

    list_pair = sorted(pair1 + pair2)
    list_impair = sorted(impair1 + impair2)

    print("Nombres pairs :", list_pair)
    print("Nombres impairs :", list_impair)

# liste_int1 = rand_list(10) 
# liste_int2 = rand_list(10)

# print("Liste d'entiers :", liste_int1 + liste_int2)
# pair_impair(liste_int1, liste_int2)

#====================================================#

def maxi(liste):

    maxi = liste[0]
    
    for index in range(1, len(liste)):
        if maxi < liste[index]:
            maxi = liste[index]
        index += 1

    return maxi

# Liste_int = sorted(rand_list(10))
# print("Liste :", Liste_int)
# print("Max :", maxi(Liste_int))

#====================================================#
import itertools

def concatain_list():
    
    global liste_int1
    global liste_int2

    result1 = [*liste_int1, *liste_int2]
    print("Exemple 1 :", result1)

    result2 = list(itertools.chain(liste_int1, liste_int2))
    print("Exemple 2 :", result2)
    
    result3 = [element for liste in [liste_int1, liste_int2] for element in liste]
    print("Exemple 3 :", result3)
    
    global liste_str1
    global liste_str2

    # s'applique uniquement à une liste de str
    # concataine l'index[i] de la liste1 a l'indexe[j] de la liste2 et incrémente i et j 
    result4 = [i + j for i, j in zip(liste_str1, liste_str2)]
    rep = [result4[i] for i in range(len(result4))]
    print("Exemple 4 :", ", ".join(map(str, rep)))
    
# liste_int1, liste_int2 = [1, 3, 5, 9, 2, 6], [4, 7, 8, 10]
# liste_str1, liste_str2 = ["maison ", "chateau-"], ["rouge", "fort"]
# concatain_list()

#====================================================#

def palindromes(liste):

    result = list(filter(lambda x: x == "".join(reversed(x)), liste))
    
    print("Palindrome(s) :", ", ".join(map(str, result)))

# liste_str = ["geeks", "geeg", "keegs", "practice", "aa"]
# print("Liste de mots :", liste_str)
# palindromes(liste_str)

#====================================================#
import collections

def anagrammes(liste):

    global mot
    result = list(filter(lambda x: collections.Counter(mot) == collections.Counter(x), liste))

    print("Anagmrme(s) de {} :".format(mot), ", ".join(map(str, result)))

# mot = "eegks"
# liste_str = ["geeks", "geeg", "keegs", "practice", "aa"]
# anagrammes(liste_str)

#====================================================#
import ast

def point_fixe(liste):

    # 
    return [ast.Index(liste[i]) for i in range(len(liste)) if i == ast.Index(liste[i])]     


# liste_int = [2, 3, 4, 3]
# print("Liste d'entiers :", liste_int)
# print("Point(s) fixe(s):", ", ".join(map(str, point_fixe(liste_int))))

#====================================================#
import collections

def major(liste):
    
    # {"keys" : values, ...} | keys -> elements de la liste | values -> nombre de fois qu'il est present dans la liste
    dico = collections.Counter(liste)
    
    # recupere le max des values du dictionaire
    el_max = max(dico.values())

    return el_max if el_max > (len(liste)/2) else -1

# liste = [1, 2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 2, 3, 3, 1, 2, 0, 0]
# print("Liste :", liste)

# if major(liste) != -1:
#     print("Elément majoritaire :", major(liste))

# else: 
#     print("Elément majoritaire inferieur à la moitier de la taille de la liste :", major(liste))

#====================================================#
import numpy as np

def iteree(liste, k):

    # decale la liste de k elements vers la droite
    decal_list = np.roll(liste, k)

    return list(map(int, decal_list))
 
# liste_int = [1,2,3,4,5]
# decalage = 3
# print("Liste d'entiers :", liste_int)
# print("Liste décalées de {} éléments :".format(decalage), iteree(liste_int, decalage))

#====================================================#
