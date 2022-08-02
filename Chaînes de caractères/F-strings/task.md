## Modèles de string

Un modèle de string, ou f-string, est une string qui est préfixée avec 'f' ou 'F'.
Ces strings peuvent contenir des champs de remplacement, qui sont délimités par des crochets `{}`.

Les parties de la string en dehors des crochets sont traitées littéralement.

Les caractères d'échappement sont décodés comme dans une string normale.
Les expressions de remplacement peuvent contenir des retours à la ligne mais ne peuvent pas contenir de commentaires. 
Chaque expression est évaluée dans le contexte où la string apparaît, dans l'ordre de gauche à droite.

Voici quelques exemples :
```python
name = "Fred"
f"He said his name is {name}."
```
```text
'He said his name is Fred.'
```

Il y a d'autres choses particulières que vous pouvez faire avec les f-strings, par exemple :
```python
f"{name.lower()} is funny."
```

```text
'fred is funny.'
```

Pour plus d'information avec les modèles, vous pouvez consulter la <a href="https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals">Documentation Python</a>.

### Tâche
Essayez de créer une f-string vous-même. Essayez ensuite de lancer le code pour voir ce qui s'affiche.

<div class="hint">La valeur affectée à la variable <code>name</code> doit être une string,
et doit donc être entre caractère de citation, tel que : <code>'Max'</code>.</div>

