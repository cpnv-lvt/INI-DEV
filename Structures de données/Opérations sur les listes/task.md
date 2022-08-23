## Opération sur les listes

Contrairement aux strings, les listes font partie des types mutables,
c'est-à-dire qu'il est possible de modifier leur contenu en utilisant `lst[index] = new_item`.

```python
# Il y a quelque chose de faux ici
cubes = [1, 8, 27, 65, 125]
# Le cube de 4 est 64 et pas 65 !
4 ** 3
```
```python
# Remplace la mauvaise valeur
cubes[3] = 64
[1, 8, 27, 64, 125]
```

Vous pouvez ajouter de nouveaux éléments à la fin de la liste en utilisant la méthode `append()` ou la concaténation.

```python
squares = [1, 4, 9, 16, 25]
squares.append(6**2)
[1, 4, 9, 16, 25, 36]
```

Vous en apprendrez plus à propos des méthodes de liste sur <a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists">cette page</a>.

### Tâche
Remplacez `"dino"` par `"dinosaur"` dans la liste `animals`.

<div class='hint'>Utilisez l'indexation de liste et l'assignation de valeur.</div>
