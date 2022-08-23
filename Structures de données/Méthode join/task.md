## La méthode join()

La méthode `.join()` est, en réalité,
une méthode de string mais nous ne l'abordons que maintenant, car elle nécessite la compréhension d'objet itérable,
tels que les strings, les listes et les tuples.

Cette [méthode](https://docs.python.org/3/library/stdtypes.html#str.join)
offre un moyen flexible de créer des strings à partir d'objets itérables. 

Elles joint chaque éléments d'un objet itérable (listes, strings ou tuples)
avec une string servant de séparateur (la string par laquelle la méthode `join()` est appelée) et retourne la string concaténée.

Une `TypeError` est levée si l'objet itérable contient des valeurs qui ne sont pas des strings.

La syntaxe de la méthode `join()` ressemble à ça :

```python
string.join(iterable)
```

Exemples :

```python
# Une string itérable
string_ = 'abcde'
# Un tuple itérable
tuple_ = ('aa', 'bb', 'cc')
# Une liste itérable
list_ = ['Python', 'programming language']

# Join avec le séparateur ' + '
print(' + '.join(string_))
# Join avec le séparateur ' = '
print(' = '.join(tuple_))

sep = ' is a '
# Join avec le séparateur ' is a '
print(sep.join(list_))
```
```text
a + b + c + d + e
aa = bb = cc
Python is a programming language
```

### Tâche
Attribuez une valeur à la variable `joined` de sorte que l'instruction `print` imprime ce qui suit :
```text
I like apples and I like bananas and I like peaches and I like grapes
```

<div class="hint">Regardez attentivement les exemples et faîtes de même !</div>
<div class="hint"><code>fruits</code> est votre objet itérable, et <code>separator</code> est le séparateur.</div>
