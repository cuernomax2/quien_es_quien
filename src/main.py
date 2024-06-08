from pyswip import Prolog
import random
from collections import defaultdict

prolog = Prolog()
prolog.consult("main.pl")

def character_to_find(characters):
    character_to_find = random.choice(characters)
    return character_to_find


def board(remaining_characters):
    personajes_restantes = 0

    print("Personajes restantes:")
    for personaje in remaining_characters:
        print(f"{personaje["Nombre"]}")
        personajes_restantes +=1
    print(f"Quedan {personajes_restantes} personajes en el tablero")
    print("--------------------------------------")


def question(win_condition, characteristic):
    if characteristic in win_condition["Caracteristicas"]:
        return True
    else:
        return False


def characteristics(characters, selector):
    caracteristica_count = defaultdict(int)
    
    for p in characters:
        for c in p["Caracteristicas"]:
            caracteristica_count[c] += 1

    sorted_caracteristicas = sorted(caracteristica_count.items(), key=lambda item: item[1], reverse=True)

    if selector == 1:
        return sorted_caracteristicas
    
    else:
        middle_index = len(sorted_caracteristicas) // 2
        return sorted_caracteristicas[middle_index][0]


if __name__ == "__main__":
    question_counter = 0
    characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    remaining_characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    win_condition = character_to_find(remaining_characters)

    board(characters)
    print(f"Personaje objetivo --> {win_condition}")
    print("--------------------------------------")
    #print(characteristics(characters, 1)) #Debugging + info
    print("--------------------------------------")
    print(characteristics(characters, 420))
    question(win_condition, characteristics(characters, 420))