## Dictionnaires

Un dictionnaire est similaire à une liste, sauf que pour accéder aux valeurs, on utilise des clefs plutôt que des index.
Une clef peut être ne n'importe quel type immuable :
- Les strings et les nombres peuvent toujours être des clefs.
- Les tuples peuvent être utilisés comme clef seulement s'ils ne contiennent que des objets immuables.
- Il n'est pas possible d'utiliser des listes comme clefs.

Considérez un dictionnaire comme un ensemble de paires de <code>clef: valeur</code>
avec la condition que les clefs doivent être uniques au sein du même dictionnaire.

Les dictionnaires sont englobés dans des accolades, par exemple : `dct = {'key1' : "value1", 'key2' : "value2"}`.

Une paire d'accolades créera un dictionnaire vide : `{}`.

Un dictionnaire peut également être créé avec le constructeur `dict` :
```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
print(a == b == c)
```
```text
True
```

Vous pouvez accéder à une valeur dans un dictionnaire de la même façon que pour une liste,
il suffit de fournir un clef plutôt qu'un index.

Vous trouverez plus d'informations sur les dictionnaires 
<a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">ici</a>.

### Tâche
Ajoutez le numéro `570` de Jared (`"Jared"`) au carnet de contacts.

Supprimez le numéro de Gerard du carnet de contacts.

Affichez le numéro de Jane depuis le carnet de contacts.

<div class='hint'>Utilisez l'indexation de dictionnaire, par exemple, <code>dct[clef]</code></div>
