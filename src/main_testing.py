def main():
    num_preguntas = 0

    # Obtenemos el personaje a adivinar.
    personaje_objetivo = eleccion_personaje()
    print(f"El personaje a adivinar es: {personaje_objetivo['Nombre']} ({personaje_objetivo['Caracteristicas']})")

    # Realizamos una consulta Prolog para obtener todos los personajes del tablero al iniciar la partida y los imprimimos.
    personajes_iniciales = list(prolog.query("personaje(Nombre,Caracteristicas)"))
    print("\n\n<----------------------------------------------------->")
    print("Personajes del tablero: ")

    # Repetimos el bucle hasta que solo quede un único personaje.
    while len(personajes_iniciales) > 1:
        
        tablero(personajes_iniciales)
        personajes_filtrados = []

        # Determinamos la característica a preguntar.
        caracteristica_pregunta = caracteristica(personajes_iniciales)
        print(f"\n¿Tu personaje tiene {caracteristica_pregunta}?")

        # Filtramos los personajes según la respuesta.
        if pregunta(personaje_objetivo, caracteristica_pregunta):
            print(f"Sí, tiene {caracteristica_pregunta}\n")
            personajes_filtrados = [p for p in personajes_iniciales if caracteristica_pregunta in p['Caracteristicas']]
        else:
            print(f"No, no tiene {caracteristica_pregunta}\n")
            personajes_filtrados = [p for p in personajes_iniciales if caracteristica_pregunta not in p['Caracteristicas']]

        personajes_iniciales = personajes_filtrados
        num_preguntas += 1

    # Imprimimos el personaje restante, que debería ser el objetivo, y el número de preguntas necesarias para adivinarlo.
    print(f"El personaje es: {personajes_iniciales[0]}")
    print(f"Número de preguntas: {num_preguntas}")
