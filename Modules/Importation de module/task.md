## Importation de module

Lorsque votre programme devient de plus en plus grans, vous aurez peut-être envie de séparer celui-ci en 
plusieurs fichiers afin de mieux l'organiser et le maintenir. Vous aurez peut-être envie d'utiliser une de vos fonctions 
dans un autre programme sans avoir à récrire celle-ci.

Les modules dans Python sont en fait de simple fichier avec l'extension `.py` contenant des définition et 
instruction python. Les modules sont importés dans votre fichier via le mot clé `ìmport` et le nom du module sans
l'extension `.py`.

Disons que vous avez écrit un script s'appelant `my_funcs.py` avec à l'intérieur du fichier des fonctions (`func1`, `func2`, 
etc.). Maintenant, si vous voulez utiliser ces fonctions dans un autre script qui se trouve dans le même dossier, vous pouvez
le faire avec l'instruction `import my_funcs`. Les fonctions ne seront pas directement accessibles, il vous faudra utiliser 
le nom du module avant, comme :
```python
my_funcs.func1()
```

Les modules peuvent importer d'autres modules. Par convention, l'import de modules se fait en début de fichier.

Vous pouvez trouver plus d'information sur les modules en python en lisant  [cette section](https://docs.python.org/3/tutorial/modules.html) 
de la documentation de Python. 

## task
Dans l'éditeur de code, importer le module `calculator` et créez une instance de la classe `Calculator` (`calc`).
Utilisez la méthode `add` définie dans `calculator` à l'intérieur d'une boucle pour ajouter les nombres de 0 à 99.

<div class='hint'>Utilisez le mot clé <code>import</code> et la référence <code>calculator</code>.</div>
<div class='hint'>Accédez à la fonction depuis le module en utilisant la syntax <code>module.function()</code>.</div>
<div class="hint">N'oubliez pas de fournir un argument à la fonction.</div>

