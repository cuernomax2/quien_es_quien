from pyswip import Prolog
import random
from collections import defaultdict

prolog = Prolog()
prolog.consult("main.pl")

def character_to_find(characters):
    character_to_find = random.choice(characters)
    return character_to_find


def question(win_condition, characteristic):
    if characteristic in win_condition["Caracteristicas"]:
        return True
    else:
        return False
    

def board(remaining_characters):
    personajes_restantes = 0

    print("Personajes restantes:")
    for personaje in remaining_characters:
        print(f"{personaje["Nombre"], personaje["Caracteristicas"]}")
        personajes_restantes +=1
    print(f"\nQuedan {personajes_restantes} personajes en el tablero")
    print("--------------------------------------")


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

    print(f"Personaje objetivo --> {win_condition}")
    print("--------------------------------------")

    while len(characters) > 1:
        candidate_characters = []
        question_to_ask = characteristics(characters)

        board(characters)

        if question(win_condition, question_to_ask) == True:
            print(f"Yes, he does have {question_to_ask}\n")
            for p in characters:
                if question_to_ask in p['Caracteristicas']:
                    candidate_characters.append(p)
        else:
            print(f"No, he does not have {question_to_ask}\n")
            for p in characters:
                if question_to_ask not in p['Caracteristicas']:
                    candidate_characters.append(p)

        characters = candidate_characters
        question_counter += 1

    # Imprimimos el personaje que queda y que debería ser el mismo al personaje objetivo, también mostramos el número de preguntas que hemos necesitado para adivinarlo.
    print(f"The character is: {characters}")
    print(f"Number of questions asked: {question_counter}")
