import random
import collections

#===============#

def rand_list(n):
    return random.sample(range(-10, 10), n)

# print(rand_list(10))

#===============#

def pair_impair(liste):

    pair = filter(lambda x: x % 2 == 0, liste)
    impair = filter(lambda x: x % 2 == 1, liste)

    print("Nombres pairs :", sorted(list(pair)))
    print("Nombres impairs :", sorted(list(impair)))

# print("Liste :", sorted(rand_list(10)))
# pair_impair(rand_list(10))

#===============#

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

#===============#

def concatain_list(l1, l2):
    return sorted(l1+l2)

# liste1, liste2 = [1, 3, 5, 9, 2, 6], [4, 7, 8, 10]
# print(concatain_list(liste1, liste2))

#===============#

def palindromes(liste):

    result = list(filter(lambda x: x == "".join(reversed(x)), liste))

    print("Palindromes :", ", ".join(map(str, result)))

# liste_str = ["geeks", "geeg", "keegs", "practice", "aa"]
# palindromes(liste_str)

#===============#

def anagrammes(liste):

    global mot
    result = list(filter(lambda x: (collections.Counter(mot) == collections.Counter(x)), liste))

    print("Anagrammes de", mot, ":", ", ".join(map(str, result)))

# mot = "eegks"
# anagrammes(liste_str)
