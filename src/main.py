from pyswip import Prolog
import random
from collections import Counter

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

def characteristic(lista):
    contador_caracteristicas = 0
    todas_las_caracteristicas = []

    for p in lista:
        for c in p["Caracteristicas"]:
            todas_las_caracteristicas.append(c)
    
    contador_caracteristicas = Counter(todas_las_caracteristicas)
    contador_caracteristicas = sorted(contador_caracteristicas.items(), key=lambda i: i[1], reverse=True)

    return contador_caracteristicas[int(len(contador_caracteristicas)/2)][0]

if __name__ == "__main__":
    question_counter = 0
    characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    remaining_characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    win_condition = character_to_find(remaining_characters)


    board(characters)
    print(f"Personaje objetivo --> {win_condition}")

    question(win_condition, characteristic)


