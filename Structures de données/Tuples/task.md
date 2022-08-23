## Tuples

Les tuples sont un autre type de données pour grouper différentes données.
Ils sont quasi identiques aux listes.
La seule différence significative est que les tuples sont immuables.

<div class='hint'>Il n'est pas possible d'ajouter, de modifier ou de supprimer des éléments dans un tuple.</div>

Les tuples sont construits en séparant les éléments par des virgules, englobés par des parenthèses. 
Par exemple : 

```python
('a', 'b', 'c')
```
 
Dans les cas spéciaux, il y a la construction de tuples contenant 0 ou 1 élément.
Les tuples vides sont construits avec des parenthèses vides,
alors qu'un tuple avec un unique élément est construit par la valeur suivie d'une virgule. C'est-à-dire :

```python
empty = ()
singleton = 'hello',    # <-- attention à la virgule !
len(empty)
```
```text
0
```
```python
len(singleton)
```
```text
1
```
```python
singleton
```
```text
('hello',)
```

L'instruction `t = 12345, 54321, 'hello!'` est un exemple de regroupement par tuple :
les valeurs `12345`, `54321` et `hello!` sont regroupées dans un tuple.

D'autres méthodes de liste sont applicables aux tuples et vous pouvez en apprendre plus sur les tuples 
<a href="https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences">ici</a>.


### Tâche
Afficher la longueur du tuple `alphabet`. Puis créez un tuple avec pour unique élément `'fun_tuple'`.
Vous pouvez lancer le code pour voir ce qui est affiché.

<div class='hint'>Utilisez la fonction <code>len()</code>.</div>

<div class='hint'>N'oubliez pas la virgule pour le tuple à un seul élément.</div>
