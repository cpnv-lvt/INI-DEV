## Listes imbriquées

Une liste peut contenir n'importe quel objet, même d'autres listes (sublists).
Dans ce cas de figure, on les nomme listes imbriquées (nested list).

Vous pouvez utiliser les listes imbriquées pour arranger les données en structures hiérarchiques.

Une liste imbriquée peut être créée en séparant des listes par des virgules :

```python
nested_list = [[1, 2, 3], [4, 5], 6]
```

Vous pouvez accéder aux éléments d'une liste imbriquée en utilisant les index comme auparavant :

```python
print(nested_list[1])
print(nested_list[2])
```
Résultat :
```text
[4, 5]
6
```
Vous pouvez accéder aux éléments d'une sublist en utilisant plusieurs index.
Pour accéder au chiffre `1` de la `nested_list`, utilisez l'index `0` deux fois.
En premier, vous accèderez à l'élément `[1,2,3]`, ensuite, avec le deuxième index,
vous accèderez au premier élément de cette sublist :

```python
print(nested_list[0][0])
```
Résultat :
```text
1
```

### Tâche
Dans l'éditeur de code,
utilisez l'indexation pour accéder et afficher les éléments `9` et `10` de la liste imbriquée `my_list`.

<div class="hint">Si vous êtes bloqué, relisez bien la description. Tout est dedans.</div>
