count = 0

while True:  # Cette condition ne peut pas être faux
    print(count)
    count += 1
    if count >= 5:
        break           # Quitte la boucle si count >= 5


zoo = ["lion", "tiger", "elephant", "giraffe", "python"]
while True:                         # Cette condition ne peut pas être faux
    animal = zoo.pop()       # Extrait un élément depuis la fin de la liste
    print(animal)
    # Ajouter une condition pour quitter la boucle
        # Quitter la boucle

print(zoo)
