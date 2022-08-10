## Boucles imbriquées

Une boucle imbriquée est en faite une boucle dans une boucle. La boucle intérieur est exécutée
à chaque itération de la boucle principale.


```python
adjectives = ["black", "stylish", "expensive"]
clothes = ["jacket", "shirt", "boots"]

for x in adjectives:
  for y in clothes:
    print(x, y)
```
Output:
```text
black jacket
black shirt
black boots
stylish jacket
stylish shirt
stylish boots
expensive jacket
expensive shirt
expensive boots
```
<details>

Notez que n'importe quel type de boucle permet d'être imbriquée.
Par exemple, la boucle [`while` loop](course://Boucles/While loop) (voir chapitre sur la boucle while) 
peut être imbriquée à l'intérieur d'une boucle `for` ou vice et versa.
</details>

On vous donne un plateau du tic-tac-toe de taille 3x3, votre tâche est d'imprimer chaque position. 
Les coordonnées de chaque côté seront enrigistrés dans la liste `coordinates`. La sortie doit être :
```text
1 x 1
1 x 2
1 x 3
2 x 1
...
```
Et ceci pour chaque combinaison de coordonées.

<div class="hint">

Dans une boucle imbriquée `for`, énuméré chaque élément de la liste en utilisant une autre variable telque (`coordinate2`).
</div>
