from pyswip import Prolog
import random

prolog = Prolog()
prolog.consult("main.pl")

def character_to_find():
    characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    character_to_find = random.choice(characters)
    return character_to_find


if __name__ == "__main__":
    characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    win_condition = character_to_find()
    print(f"Personaje objetivo --> {win_condition}")
    question_counter = 0


