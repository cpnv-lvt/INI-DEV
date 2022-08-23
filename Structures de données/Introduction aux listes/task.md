## Introduction aux listes

Python a plusieurs types de donnée utilisés pour grouper des données ensemble.
Le type le plus polyvalent est la liste,
qui peut être écrite en une série de valeurs (éléments) séparées par des virgules et englobées dans des crochets,
par exemple : `lst = [item1, item2]`. 

Les listes peuvent contenir des éléments de types différents, cependant,
par convention, tous les éléments d'une liste sont d'un même type.

Tout comme les strings, les listes peuvent être indexées et découpées (voir la [Leçon 3](course://Chaînes de caractères/Découpage de string)).
Toutes les opérations de découpage retourneront une nouvelle liste contenant les éléments attendus.

Les listes supportent également les opérations comme la concaténation :

```python
squares = [1, 4, 9, 16, 25]
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Vous pouvez en apprendre plus sur les listes en lisant <a href="https://docs.python.org/3.9/tutorial/introduction.html#lists">cette page</a>.

### Tâche
Utilisez le découpage pour afficher `[4, 9, 16]`.  

<div class='hint'>
Le découpage de liste fonctionne exactement comme pour les strings : <code>list[index1:index2]</code>.

N'oubliez pas que l'élément avec l'index <code>index2</code> ne sera pas inclus !
</div>
