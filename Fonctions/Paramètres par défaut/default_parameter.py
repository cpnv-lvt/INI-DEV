def multiply_by(a, b=2, c=1):
    return a * b + c


print(multiply_by(3, 47, 0))  # Appel de la fonction en utilisant tous les parameters
print(multiply_by(3, 47))  # Appel de la fonction en utilisant les valeurs par défaut pour c
print(multiply_by(3, c=47))  # Appel de la fonction en utilisant les valeurs par défaut pour b
print(multiply_by(3))  # Appel de la fonction en utilisant les valeurs par défaut pour b et c
print(multiply_by(a=7))  # Appel de la fonction en utilisant les valeurs par défaut pour b et c


def hello(???):
    print(f"Hello {subject}! My name is {name}")


hello("PyCharm", "Jane")  # Appel de la fonction "hello" avec "PyCharm" comme 1er paramètre et "Jane" comme nom
hello("PyCharm")  # Appel de la fonction "hello" avec "PyCharm" comme 1er paramètre et la valeur par default pour le nom
