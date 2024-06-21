from pyswip import Prolog
import random
from collections import defaultdict
import operator

prolog = Prolog()
prolog.consult("main.pl")

def character_to_find(characters): #Define character to find using random
    character_to_find = random.choice(characters)
    return character_to_find


def question(win_condition, characteristic): #Check is character snet to the function has the characteristic asked
    if characteristic in win_condition["Caracteristicas"]:
        return True
    else:
        return False


def available_characteristics(characters):
    characteristics_set = set()  # Use a set to avoid duplicates
    for character in characters:
        for characteristic in character.get("Caracteristicas", []):
            characteristics_set.add(characteristic)
    return list(characteristics_set)


def board(remaining_characters): #Prints the board containing all the characters inputed
    personajes_restantes = 0

    print("Personajes restantes:")
    for personaje in remaining_characters:
        print(f"\n{personaje["Nombre"], personaje["Caracteristicas"]}")
        personajes_restantes +=1
    print(f"\nQuedan {personajes_restantes} personajes en el tablero")
    print("--------------------------------------")


def characteristics(characters): #Optimized function to check average characteristic in remaining characters
    caracteristica_count = defaultdict(int)
    
    for a in characters:
        for b in a["Caracteristicas"]:
            caracteristica_count[b] += 1

    sorted_characteristics = sorted(caracteristica_count.items(), key=operator.itemgetter(1), reverse=True)
    middle_index = len(sorted_characteristics) // 2
    return sorted_characteristics[middle_index][0]


if __name__ == "__main__":
    questions_user = []
    questions_computer = []
    question_counter_user = 0
    question_counter_computer = 0
    characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    win_condition = character_to_find(characters)

    play_against_computer = input("Do you want to play against the computer? y/n --> ")

    if play_against_computer.lower() == "y":
        valid_characteristics = available_characteristics(characters)
        remaining_characters = characters.copy()
        board(characters)
        print("--------------------------------------")

        while len(remaining_characters) > 1:
            user_input = input(f"Ask one of the following characteristics: {valid_characteristics} --> ")
            if user_input in valid_characteristics:
                remaining_characters = []
                if not question(win_condition, user_input):
                    print(f"No, he does not have {user_input}\n")
                    for a in characters:
                        if user_input not in a['Caracteristicas']:
                            remaining_characters.append(a)
                else:
                    print(f"Yes, he does have {user_input}\n")
                    for b in characters:
                        if user_input in b['Caracteristicas']:
                            remaining_characters.append(b)

                questions_user.append(user_input)
                characters = remaining_characters.copy()
                valid_characteristics = available_characteristics(characters)
                question_counter_user += 1
                board(characters)
            else:
                print("Invalid input. Please try again.")

        characters = list(prolog.query("personaje(Nombre, Caracteristicas)"))
        remaining_characters = characters.copy()

        while len(characters) > 1:
            remaining_characters = []
            question_to_ask = characteristics(characters)

            if question(win_condition, question_to_ask) == False:
                print(f"No, he does not have {question_to_ask}\n")
                for a in characters:
                    if question_to_ask not in a['Caracteristicas']:
                        remaining_characters.append(a)

            else:
                print(f"Yes, he does have {question_to_ask}\n")
                for b in characters:
                    if question_to_ask in b['Caracteristicas']:
                        remaining_characters.append(b)

            questions_computer.append(question_to_ask)
            characters = remaining_characters
            question_counter_computer += 1

    else:     
        print(f"Personaje objetivo --> {win_condition}")
        print("--------------------------------------")

        while len(characters) > 1:
            remaining_characters = []
            question_to_ask = characteristics(characters)

            board(characters)

            if question(win_condition, question_to_ask) == False:
                print(f"No, he does not have {question_to_ask}\n")
                for a in characters:
                    if question_to_ask not in a['Caracteristicas']:
                        remaining_characters.append(a)

            else:
                print(f"Yes, he does have {question_to_ask}\n")
                for b in characters:
                    if question_to_ask in b['Caracteristicas']:
                        remaining_characters.append(b)
            questions_computer.append(question_to_ask)
            characters = remaining_characters
            question_counter_computer += 1

    print(f"The character is: {characters[0]['Nombre']}")
    print(f"Characteristics asked by user: {questions_user}")
    print(f"Number of questions asked by the user: {question_counter_user}")
    print(f"Characteristics asked by user: {questions_computer}")
    print(f"Number of questions asked by the computer: {question_counter_computer}")
