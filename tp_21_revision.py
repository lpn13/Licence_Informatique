import random
import collections

#====================================================#

def rand_list(n):
    return random.sample(range(-10, 10), n)

# print(rand_list(10))

#====================================================#

def pair_impair(list1, list2):

    pair1 = list(filter(lambda x: x % 2 == 0, list1))
    pair2 = list(filter(lambda x: x % 2 == 0, list2))
    
    impair1 = list(filter(lambda x: x % 2 == 1, list1))
    impair2 = list(filter(lambda x: x % 2 == 1, list2))

    list_pair = sorted(pair1 + pair2)
    list_impair = sorted(impair1 + impair2)

    print( "Nombres pairs :", list_pair)
    print("Nombres impair :", list_impair)

# liste_int1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# liste_int2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

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

# Liste_int = [-5, 6, 12, -34, 9, 987]
# print("Liste :", Liste_int)
# print("Max :", maxi(Liste_int))

#====================================================#

def concatain_list(l1, l2):
    return sorted(l1+l2)

# liste1, liste2 = [1, 3, 5, 9, 2, 6], [4, 7, 8, 10]
# print(concatain_list(liste1, liste2))

#====================================================#

def palindromes(liste):

    result = list(filter(lambda x: x == "".join(reversed(x)), liste))

    print("Palindrome(s) :", ", ".join(map(str, result)))

# liste_str = ["geeks", "geeg", "keegs", "practice", "aa"]
# print("Liste de mots :", liste_str)
# palindromes(liste_str)

#====================================================#

def anagrammes(liste):

    global mot
    result = list(filter(lambda x: collections.Counter(mot) == collections.Counter(x), liste))

    print("Anagmrme(s) de {} :".format(mot), ", ".join(map(str, result)))

# mot = "eegks"
# liste_str = ["geeks", "geeg", "keegs", "practice", "aa"]
# anagrammes(liste_str)
