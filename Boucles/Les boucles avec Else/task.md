## Les boucles avec Else

Nous avons déjà vu que le terme `break` sort de la boucle `for` ou `while`.

Python permet aussi à une boucle d'avoir une clause `else`. Cette partie sera exécutée à la fin de la boucle sur un itérable
(pour la boucle `for`) ou losque la condition devient `False`dans une boucle `while`, mais pas losque l'on quitte une boucle 
avec `break`. Regarder l'exemple ci-dessous qui recherche les nombres premiers :


```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```
```text
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

Dans le code ci-dessus, la claude `else` est attachée à la boucle `for` et pas a un teste logique `if`.

Rappelez-vous que `else` après un `if`n'est PAS exécuté  si l'expression après `if` est vrai (`True`), alors que dans le
cas d'une boucle, un `else` sera exécuté à la fin de la boucle (sauf si celle-ci est terminée par un `break`).

# task

Dans l'éditeur de code, ajoutez deux lignes de code à la seconde boucle afin d'être sûr que la boucle imprime seulement 
les nombres 1 et 2 and n'imprime jamais la phrase `"for loop is done"`.

<div class="hint">La boucle doit se terminer sur le nombre 3.</div>
