## Arguments et paramètres d'une fonction

Les paramètres d'une fonction sont définis à l'intérieur des parenthèses `()` juste après le nom de la fonction. 
Un paramètre joue le rôle d'une variable pour l'argument passé à la fonction.

Les termes paramètres et arguments font référence au même chose : l'information qui est passé à une fonction. 
Cependant, un paramètre est une variable listée à l'intérieur de la déclaration d'une fonction (dans les parenthèses), 
alors qu'un argument est la valeur qui est envoyée à la fonction lorsqu'elle est appelée.

Par défaut, une fonction doit être appelée avec le nombre d'arguments correct. Si votre fonction demande deux arguments,
vous devez lui fournir deux arguments :

```python
def my_function(name, surname):
    print(name + " " + surname)

my_function("Jon", "Snow")
```
Résultat:
```text
Jon Snow
```
Sinon, si vous fournissez seulement un argument lors de son appel :
```python
my_function("Sam")
```
une erreur de telque :`TypeError` sera appelée :
```text
TypeError                                 Traceback (most recent call last)
<ipython-input-29-40eb74e4b26a> in <module>
----> 1 my_function('Jon')

TypeError: my_function() missing 1 required positional argument: 'surname'
```
### Task
Dans l'éditeur de code, définissez une fonction qui imprime le carré d'un nombre.r.  

<div class='hint'>Ajoutez un <code>x</code> comme paramètre à l'intérieur des  parenthèses dans la définition de la fonction.</div>
