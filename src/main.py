from pyswip import Prolog
import random
from collections import defaultdict

prolog = Prolog()
prolog.consult("main.pl")

def character_to_find(characters):
    character_to_find = random.choice(characters)
    return character_to_find


def board(remaining_characters):
    print("Personajes restantes:")
    for personaje in remaining_characters:
        print(f"{personaje["Nombre"]}")
    print("--------------------------------------")


def question(win_condition, characteristic):
    if characteristic in win_condition["Caracteristicas"]:
        return True
    return False


def characteristics(characters):
    caracteristica_count = defaultdict(int)
    
    for p in characters:
        for c in p["Caracteristicas"]:
            caracteristica_count[c] += 1

    sorted_caracteristicas = sorted(caracteristica_count.items(), key=lambda item: item[1], reverse=True)
    
    middle_index = len(sorted_caracteristicas) // 2
    return sorted_caracteristicas[middle_index][0]


if __name__ == "__main__":
    question_counter = 0
    characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    remaining_characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    win_condition = character_to_find(remaining_characters)

    board(characters)
    print(f"Personaje objetivo --> {win_condition}")
    print(characteristics(characters))
    question(win_condition, characteristics(characters))