from pyswip import Prolog

prolog = Prolog()
prolog.assertz("personaje('John Doe', ['Tall', 'Smart'])")

for result in prolog.query("personaje(X, Y)"):
    print(result)