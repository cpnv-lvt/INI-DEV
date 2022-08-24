## Paramètres par défaut

Il est possible de définir une fonction avec un nombre variable d'arguments. Il y a trois formes qui peuvent être combinés.
La forme la plus pratique est de définir une valeur par défaut pour l'un ou plusieurs des arguments. Cela permet de définir une 
fonction qui sera appelée avec moins d'arguments. Par exemple, vérifiez la première fonction dans l'éditeur de code.
Cette fonction peut être appelée de différentes manières :

- en donnant que l'argument obligatoire : `a`: `multiply_by(3)`

- en donnant l'un des arguments facultatifs : `multiply_by(3, 47)`, ou `multiply_by(3, c=47)`

- ou en donnant tous les arguments : `multiply_by(3, 47, 0)`

Vous pouvez spécifier quel argument vous fournissez à votre fonction, tel que dans le troisième exemple ci-dessus avec `c=47`.
Si vous ne spécifiez rien, les valeurs seront assignées selon l'ordre présent dans la déclaration de votre fonction.
Attention, vous ne devez pas mettre d'espace entre le symbole `=` lors de la déclaration ou de l'appel.


 
Si vous voulez en savoir plus sur le sujet voici <a href="https://docs.python.org/3/tutorial/controlflow.html#default-argument-values">un lien</a>
dans le documentation Python.


### Task
Ajoutez un paramètre à la fonction `hello()`  et configurer une valeur par défaut pour le paramètre `name`.  

<div class='hint'> Spécifiez n'importe quelle valeur pour le paramètre <code>name</code>.</div>
