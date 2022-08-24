# Importation de la class Calculator depuis un autre module
from my_module import hello as hey

print(hey("User"))

calc = 'Instantiate a calculator'  # Nom `Calculator` utiliser directement sans prefix `calculator`
calc.add(2)
calc.multiply(100)
calc.divide(3)

print(calc.get_current())



