## Condition

Les instructions composées en Python contiennent (des groupes d') autres instructions; Elles affectent ou contrôlent
l'exécution de ces autres déclarations d'une manière ou d'une autre.

Le type d'instruction le plus connu est certainement l'instruction `if`.

Le mot-clé `if` est utilisé pour former une instruction conditionnelle qui exécute certaines instructions 
spécifiées après avoir vérifié si son expression est `True`.

Python utilise l'indentation pour définir des blocs de code :

```python
if value > 1000: 
    print("It's a large number!")  # bloc indenté
    a += 1                         # bloc indenté
    
print("Outside the block!")        
```

Un bloc de code commence par l'indentation et se termine par la première ligne non indentée.

Le degré d'indentation doit être cohérent tout au long du bloc.
La façon la plus simple d'indenter est d'utiliser la touche de tabulation.

Des erreurs dans l'indentation lèveront une `IndentationError`. 

Si vous n'avez qu'une seule instruction à exécuter, vous pouvez l'écrire à la même ligne que le `if`.

```python
if a > b: print("a is greater than b")
```

### Tâche
Affichez `"empty"` si la liste `tasks` est vide.
Après que la liste soit vidée, vérifiez à nouveau (potentiellement avec une autre condition !)
et affichez `'Now empty!'` si elle est vide.

<div class='hint'>Utilisez la fonction <code>len()</code> pour vérifier si <code>tasks</code> est vide.</div>
