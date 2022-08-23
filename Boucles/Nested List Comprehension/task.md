## L'imbrication de list comprehension

Une liste imbriquée est simplement une liste qui contient à l'intérieur une autre liste.
Elles sont très similaires aux [Boucles imbriquées](course://Boucles/Nested for Loop).
Voici un programme qui construit une [Liste imbriquée](course://Structures de données/Listes imbriquées) en utilisant 
des boucles imbriquées :

```python
matrix = []

for i in range(3):

    # Append an empty sublist inside the list
    matrix.append([])

    for j in range(0, 10, 2):
        matrix[i].append(j)

print(matrix)
```
Sortie:
```text
[[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]
```

Le même programme peut être écrit en une seul ligne en utilisant les listes imbriquées :

```python
matrix = [[j for j in range(0, 10, 2)] for i in range(3)]
print(matrix)
```
Sortie:
```text
[[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]
```

### Task

Créer une `matrice` de $10x10$ de tel sorte que chaque ligne (sous liste) contiennent les **caractères** 0-9 depuis une 
chaine de caractères. Utilisez la technique présenter ci-dessous afin d'écrire un code en une ligne.

<div class="hint">

suivez l'exemple dans la partie ci-dessus. Vous devez simplement utiliser une `string` comme itérable à la place 
de chaque rang ([0],[1], etc ...)
</div>



