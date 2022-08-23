## Nom d'argument


Nous avons déjà vu qu'une fonction peut être appelée  en lui founissant comme paramètre le nom d'un argument telque : `kwarg=value`.
Par exemple la fonction `cat()` que nous avons définit pour vous accèpte un argument (`food`) et trois argument optionels
(`state`, `action`, et `breed`). La fonction peut être appelée comme ci-dessous :

```python
cat('chicken')                     # 1  argument 
cat(food='chicken')                # 1 argument avec son mot clé
cat(food='fish', action='bite')    # 2 arguments avec leurs mots clés
cat(action='bite', food='fish')    # 2 arguments avec leurs mots clés
cat('beef', 'happy', 'hiss')       # 3 arguments
cat('a hug', state='purrring')     # 1 argument, 1 avec mot clé
```

Lors de l'appel d'une fonction, les mots-clés doivent suivre la position définit lors de la déclaration (en-tête de fonction).
Tous les arguments passé par mot-clé doivent correspondre au nom définit par la fonction 
(par exemple : `book` n'est pas un mot valide d'argument pour la fonction `cat`), l'ordre par contre n'est pas important.
Aucun argument ne peut recevoir plus d'une fois le même argument. Les exemple ci-dessous ne sont pas valide :
```python
cat()                              # required argument missing
cat(food='fish', 'dead')           # positional argument after a keyword argument
cat('veggies', food='nothing')     # duplicate value for the same argument
cat(actor='Johnny Depp')           # unknown keyword argument
```

### Task
Dans l'éditeur, compléter l'appel de la fonction avec les bons arguments afin d'imprimer à l'écran ce qui suit :
```text
-- This cat wouldn't growl if you gave it soup
-- Lovely fur, the Sphinx
-- It's still hungry!
```

<div class="hint">Pour les arguments à mot-clé, utiliser la syntaxe suivante <code>state='asleep'</code>.</div>
<div class="hint">L'argument obligatoire  <code>food</code> doit être en première position, à moins de le spécifier avec son mot-clé.</div>
