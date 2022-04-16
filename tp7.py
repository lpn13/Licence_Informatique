import random

#=========================================#
#=== Modélisation à partir d'une liste ===#
#=========================================#

#=== Question 1 : ===#
# Retourne une liste de taille N où tous les éléments sont nuls.
def init_ram_list(N):

    return [0] * N

#=== Question 2 : ===#
# Place au hasard N valeurs entières (tirées au hasard entre 1 et 255) dans cette mémoire.
def fill_ram_random(ram, N):

    l = [0] * ram
    index = random.sample(range(ram), N)

    for n in range(N):
        for k in range(len(index)):
            values = random.randint(1, 255)
            l[index[k]] = values

    return l

#=== Question 3 : ===#
# Place au hasard N nombres dont la valeur dépend de leur position.
def fill_ram_place(ram, N):

    index = random.sample(range(len(ram)), N)

    for i in range(len(index)):
        ram[index[i]] = index[i]
   
    return ram

#=== Question 4 : ===#
# Retourne la valeur en mémoire placée à l'adresse donnée.
def get_value_list(ram, adresse):

   return ram[adresse]

#==============================================#
#=== Modélisation à partir d'un ditionnaire ===#
#==============================================#

#=== Question 1 : ===#
# Retourne un dictionnaire contenant uniquement un élément dont la clé est 'taille' initialisée à N.
def init_ram_dict(N):

    return {"taille" : N}

#=== Question 2 : ===#
# Retourne un dictionnaire qui contient N valeurs entières (tirées au hasard entre 1 et 255) à une place tirée au hasard.
def fill_ram_random_dict(ram, N):

   dico = {"taille" : ram}
   index = random.sample(range(ram), N)
   values = random.sample(range(256),N)

   for n in range(N):
       for k in range(len(index)):
           dico[index[k]] = values[k]

   return dico

#=== Question 3 : ===#
# Place au hasard N nombres dont la valeur dépend de leur position.
def fill_ram_place_dict(ram, N):

   dico = {"taille" : ram}
   index = random.sample(range(ram), N)

   for n in range(N):
      for k in range(len(index)):
         dico[index[k]] = index[k]

   return dico

#=== Question 4 : ===#
# Retourne la valeur en mémoire placée à l'adresse donnée.
def get_value_dict(ram, adresse):

   RAM = fill_ram_place_dict(16, 5)

   return RAM.get(adresse)

#==============================#
#=== Cache Full associative ===#
#==============================#

#=== La mémoire associative ===#
# Retourne un tuple formé de trois valeurs :
# - Le mot'HIT' si le mot est dans la mémoire, 'MISS' s'il n'y est pas.
# - Le vecteur de comparaison.
# - L'indice en mémoire contenant le mot (ou None s'il n'y est pas).
def is_in(mem_asso, mot):

   list_bin = [element == mot for element in mem_asso]

   if mot in mem_asso:
      return ('Hit', list_bin, mem_asso.index(mot))

   else :
      return ('Miss', list_bin, None)

#=== La mémoire classique ===#
# Fonction qui prend en paramètre la mémoire classique et l'indice de l'élément voulu, puis qui retourne le dictionnaire associé mais avec la clé data à None si l'entrée n'est pas valide.
def get_value(mem, idx):

   if idx > len(mem): return None

   value = mem[idx]

   if not value["ok"]:
      value["data"] = None

   return value

#=== Combinaison des deux mémoires ===#
# Cette fonction retourne le tuple composé :
# - Du mot 'HIT' si la valeur est présente en cache et valide, ou 'MISS' sinon.
# - De la valeur stockée dans la mémoire classique associée ou None.
def in_cache(mem_asso, mem_class, adresse):

   cache = is_in(mem_asso, adresse)
   value = get_value(mem_class, adresse)

   if cache[0] == "Hit" and value["ok"]:
      return ("Hit", value["data"])

   return ("Miss", None)

#===========================#
#=== Cache direct-mapped ===#
#===========================#

#=== Question 1 : ===#
# Retourne un tuple composé comme pour la mémoire full associative :
# - Du mot 'HIT' si l'adresse est présente en cache et valide, ou le mot 'MISS'.
# - De la valeur présente ou None si elle n'est pas présente en cache.
def in_cache_direct_mapped(mem_class, adresse):

   if adresse > len(mem_class):
      R = get_value(mem_class, len(mem_class)-1)

      if R["ok"] == True:
         return ("Hit", R["data"])

      else:
         return ("Miss", None)

   else:
      R = get_value(mem_class, adresse)

      if R["ok"] == True:
         return ("Hit", R["data"])

      else:
         return ("Miss", None)

   return(etat, data)

#============================#
#=== Pour aller plus loin ===#
#============================#

#=== Gestion des synonymes dans la cache direct-mapped ===#
# Retourne un tuple formé :
# - Du mot 'HIT' si l'adresse est présente en cache et valide, ou le mot 'MISS'.
# - De la valeur présente ou None si elle n'est pas présente en cache.
def in_cache_direct_mapped_fixed(mem_class, adresse):

    if adresse > len(mem_class):
        return in_cache_direct_mapped(mem_class, adresse)

    if mem_class[adresse]["tag"] != 0x1:
        return in_cache_direct_mapped(mem_class, adresse)

    else:
        mem_class[adresse]["data"] = None
        return "Miss", mem_class[adresse]["data"]
        
#=== Politique de remplacement aléatoire ===#
# Si une entrée invalide existe, la fonction retourne son indice.
# S'il n'y a aucune entrée invalide, la fonction retourne aléatoirement un des indices du cache.
def replace_random(mem_asso, mem):

    for index, entree in enumerate(mem):
        if not entree["ok"]: return index

    return random.randint(0, len(mem)-1)

#=== Politique de remplacement FIFO ===#

#=== Question 1 : ===#
# Retourne la file avec la valeur ajoutée en queue.
def add_fifo(fifo, values):

    none_index = 0
    
    while none_index < len(fifo) and fifo[none_index] != None:
        none_index += 1
    
    if none_index >= len(fifo): return False
    else:
        fifo[none_index] = values
        return fifo

#=== Question 2 : ===#
# Retourne à la fois la nouvelle file sans la valeur de tête, et la valeur qui vient d'être enlevée.
def get_fifo(fifo):

    value = fifo.pop(0)
    fifo.append(None)

    return fifo, value

#=== Question 3 : ===#
# Retourne l'indice où placer la nouvelle valeur dans le cache et la file modifiée pour tenir compte de cette politique de remplacement.
# Si une entrée invalide existe, la fonction retourne son indice et la nouvelle file.
# S'il n'y a aucune entrée invalide, la fonction retourne l'indice de la donnée la plus ancienne dans le cache (celle de tête de file), et la nouvelle file.
def replace_fifo(mem, fifo):

    invalide_index = None

    for index, entree in enumerate(mem):
        if not entree["ok"]:
            invalide_index = index
            break

    if invalide_index != None:
        return invalide_index, add_fifo(fifo, invalide_index)

    else:
        value = get_fifo(fifo)[1]
        fifo = add_fifo(fifo, value)
        return value, fifo

#=== Politique de remplacement LRU ===#
# Retourne la pile LRU avec la valeur déplacée en sommet de pile.
def update_lru(pile, value):

    none_index = 0
    
    while none_index < len(pile) and pile[none_index] != None:
        none_index += 1
    none_index -= 1

    index = 0
    while pile[index] != value:
        index += 1

    pile.pop(index)
    pile.pop(none_index)
    pile.append(value)
    pile.append(None)

    return pile

#==================#
#=== Affichages ===#
#==================#

#=========================================#
#=== Modélisation à partir d'une liste ===#
#=========================================#

#=== Question 1 : ===#
RAM = init_ram_list(16)
print(RAM)

#=== Question 2 : ===#
print(fill_ram_random(16, 5))

#=== Question 3 : ===#
RAM = fill_ram_place(RAM, 5)
print(RAM)

#=== Question 4 : ===#
print(get_value_list(RAM, 5))

#================================================#
#===  Modélisation à partir d'un ditionnaire  ===#
#================================================#

#=== Question 1 : ===#
RAM = init_ram_dict(16)
print(RAM)

#=== Question 2 : ===#
print(fill_ram_random_dict(16, 5))

#=== Question 3 : ===#
print(fill_ram_place_dict(16, 5))

#=== Question 4 : ===#
print(get_value_dict(RAM, 3))
print(get_value_dict(RAM, 4))
print(get_value_dict(RAM, 10))


#================================#
#===  Cache Full associative  ===#
#================================#

#=== La mémoire associative ===#
print([4, 1, 2, 0])

print(3, is_in([4, 1, 2, 0], 3))
print(1, is_in([4, 1, 2, 0], 1))
print(0, is_in([4, 1, 2, 0], 0))


#=== La mémoire classique ===#
M = [{'ok': True, 'data': 0x44},
    {'ok': False, 'data': 0xFF},
    {'ok': True, 'data': 0x22},
    {'ok': True, 'data': 0x99}]

print(get_value(M, 3))
print(get_value(M, 1))


#=== Combinaison des deux mémoires ===#
mem_associative = [4, 1, 2, 0]
mem_classique = [{'ok': True, 'data': 0x44},
                {'ok': False, 'data': 0xFF},
                {'ok': True, 'data': 0x22},
                {'ok': True, 'data': 0x00}]

print(3, in_cache(mem_associative, mem_classique, 3))
print(1, in_cache(mem_associative, mem_classique, 1))
print(2, in_cache(mem_associative, mem_classique, 2))


#===========================#
#=== Cache direct-mapped ===#
#===========================#

#=== Question 1 : ===#
mem_classique = [{'ok': True, 'data': 0x00},
                {'ok': False, 'data': 0xFF},
                {'ok': True, 'data': 0x22},
                {'ok': True, 'data': 0x77}]

print(0, in_cache_direct_mapped(mem_classique, 0))
print(7, in_cache_direct_mapped(mem_classique, 7))
print(1, in_cache_direct_mapped(mem_classique, 1))
print(3, in_cache_direct_mapped(mem_classique, 3))


#============================#
#=== Pour aller plus loin ===#
#============================#

#=== Gestion des synonymes dans la cache direct-mapped ===#
mem_direct_mapped = [{'ok': True, 'data': 0x00, 'tag': 0x0},
                     {'ok': False, 'data': 0xFF, 'tag': 0x1},
                     {'ok': True, 'data': 0x22, 'tag': 0x0},
                     {'ok': True, 'data': 0x77, 'tag': 0x1}]

print(in_cache_direct_mapped_fixed(mem_direct_mapped, 0), 0)
print(in_cache_direct_mapped_fixed(mem_direct_mapped, 7), 7)
print(in_cache_direct_mapped_fixed(mem_direct_mapped, 1), 1)
print(in_cache_direct_mapped_fixed(mem_direct_mapped, 3), 3)


#=== Politique de remplacement aléatoire ===#
mem_associative = [4, 1, 2, 0]
mem_classique = [{'ok': True, 'data': 0x44}, 
                 {'ok': False, 'data': 0xFF},
                 {'ok': True, 'data': 0x22}, 
                 {'ok': True, 'data': 0x00}]

print(replace_random(mem_associative, mem_classique))

mem_classique = [{'ok': True, 'data': 0x44}, 
                 {'ok': True, 'data': 0xFF},
                 {'ok': True, 'data': 0x22}, 
                 {'ok': True, 'data': 0x00}]

print(replace_random(mem_associative, mem_classique))


#=== Politique de remplacement FIFO ===#

#=== Question 1 : ===#
fifo = [None, None, None, None]
print(fifo)

fifo = add_fifo(fifo, 10)
print(fifo)

fifo = add_fifo(fifo, 99)
print(fifo)

fifo = add_fifo(fifo, 2)
print(fifo)


#=== Question 2 : ===#
fifo = [10, 99, 2, None]
print(fifo)

fifo, value = get_fifo(fifo)
print(fifo, value)

fifo, value = get_fifo(fifo)
print(fifo, value)

fifo, value = get_fifo(fifo)
print(fifo, value)


#=== Question 3 : ===#
fifo = [2, 3, 0, None]
mem_classique = [{'ok': True, 'data': 0x44}, 
                 {'ok': False, 'data': 0xFF},
                 {'ok': True, 'data': 0x22}, 
                 {'ok': True, 'data': 0x00}]
print(replace_fifo(mem_classique, fifo))

mem_classique = [{'ok': True, 'data': 0x44}, 
                 {'ok': True, 'data': 0xFF},
                 {'ok': True, 'data': 0x22}, 
                 {'ok': True, 'data': 0x00}]
print(replace_fifo(mem_classique, [2, 3, 0, 1]))

mem_classique = [{'ok': True, 'data': 0x44}, 
                 {'ok': True, 'data': 0xFF},
                 {'ok': True, 'data': 0x22}, 
                 {'ok': True, 'data': 0x00}]
print(replace_fifo(mem_classique, [3, 0, 1, 2]))


#=== Politique de remplacement LRU ===#
pile = [2, 3, 0, None]

pile = update_lru(pile, 3)
print(pile)

pile = update_lru(pile, 2)
print(pile)

pile = update_lru(pile, 2)
print(pile)