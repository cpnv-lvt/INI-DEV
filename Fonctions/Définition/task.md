## Définition

Les fonctions permettent de découper votre code en petite partie utile, plus lisible et surtout réutilisable.
Le mot clé `def` commence la définition d'une nouvelle fonction. Ce mot sera suivi du nom de la fonction et 
 entre parenthèse d'une liste de paramètres (qui peut être vide) et se termine avec le caractère `:`. Le code de la fonction commence à la ligne suivante 
et doit être indenté. 

Le code contenu dans une fonction ne sersa executé que lorsque celle-ci est appelée. Pour appeler une fonction, utiliser 
son nom avec les parenthèses.

```python
def my_function():  # définition d'une fonction
  print("Hello from a function")

my_function()  # appel de la fonction
```


Pour en savoir plus sur la définition d'une fonction sur <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">cette page</a> de la documentation de Python.

### Task
 - Appelez la fonction `my_function` à l'intérieur de la boucle afin de l'invoquer 5 fois.
 - Définissez une fonction qui remplace les appels duplicer de `print` dans le fichier.  

<div class='hint'>Utilisez les <code>()</code> pour appelez la fonction  <code>my_function</code>.</div>
<div class='hint'>Utilisez le mot clé <code>def</code> pour définir la <code>fonction</code>.</div>
