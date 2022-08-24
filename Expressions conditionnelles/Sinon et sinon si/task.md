## Sinon et sinon si

Les instruction `elif` et `else` complètent l'instruction `if`.

Il peut y avoir de zéro à plusieurs instructions `elif` et l'instruction `else` est optionnelle,
mais ne peux apparaître qu'une fois.

L'instruction `elif` est un raccourci pour `else if`, utilisé dans d'autres langages,
et est très pratique pour éviter trop d'indentation (en faisant des if dans des if).

<div class="hint">Une séquence <code>if … elif … elif …</code> est un substitut aux instructions <code>switch</code> ou 
<code>case</code> que l'on trouve dans d'autres langages, comme le C.</div>

En exécution conditionnelle,
une seule des parties est sélectionnée en évaluant les expressions une par une jusqu'à ce qu'une soit trouvée
être "vrai". Ensuite, cette suite est exécutée et aucune autre partie de l'instruction "if" n'est évaluée.
Si toutes les expressions sont fausses, ce qui se trouve dans le `else`, s'il est présent, est exécuté.


```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
```text
a is greater than b
```

### Tâche
Affichez `True` si `name` est égal à `"John"` ou `False` sinon.  

<div class='hint'>Utilisez l'instruction <code>if</code> et l'opérateur <code>==</code>.</div>
<div class='hint'>Utilisez l'instruction <code>else</code>.</div>
