## Découpage

Le découpage est utilisé pour extraire plusieurs caractères (une substring) d'une string.
La syntaxe est similaire à l'indexation, mais au lieu d'un seul index, vous utiliserez deux index (nombres) séparés par `:`,
par exemple, `str[ind1:ind2]`.

Ces deux index correspondent au début et à la fin de la substring.

Voici un visuel de comment fonctionne le découpage en Python :

```text
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

##### Exemple
<pre><code>
str[start:end] # Commence par start jusqu'à end - 1
str[start:]    # Commence par start jusqu'à la fin
str[:end]      # Commence par le début jusqu'à end - 1
str[:]         # Une copie de la chaîne de caractères entière
</code></pre>

### Tâche
Utilisez le découpage pour récupérer `"Python"` de la variable `monty_python`.  

<div class='hint'>Vous pouvez laisser un des deux index vides.</div>
