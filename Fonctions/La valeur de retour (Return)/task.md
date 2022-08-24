## La valeur de retour (Return)

Les fonctions peuvent retourner une valeur à celui qui l'a appelé, en utilisant le mot clé `return` . 
Vous pouvez utiliser la valeur retournée en l'assignant à une variable ou simplement en l'imprimant. En fait, 
une fonction qui n'emploi pas le mot `return` renvoi une valeur. Cette valeur est appelée  `None` (C'est un nom interne à python).
Écrire la valeur `None` est normalement supprimé par l'interpréteur python, si vous voulez le voir, vous pouvez appeler
la fonction comme tel : `print(some_func())`.

><i>La première déclaration d'une fonction peut être une chaine de caractères; cette chaine sert à documenter votre fonction.   
On l'appel docstring (vous trouverez plus d'information sur docstrings dans la section :
<a href="https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings">Documentation Strings</a>
de la documentation Python). C'est une bonne pratique d'inclure un docstrings dans votre code.</i>

Dans la suite de Fibonacci, les deux premiers nombres sont `1` et `1`, chaque séquence suivante est la somme des deux précédents.

### Task
Écrire une fonction qui retourne la liste des nombres de la suite de Fibonacci jusqu'à `n` .  

<div class='hint'>Initialise <code>b</code> avec 1.</div>
<div class='hint'>Mettez à jour <code>b</code> avec <code>a + b</code>.</div>
<div class='hint'>Mettez à jour <code>a</code> avec <code>tmp_var</code>.</div>


