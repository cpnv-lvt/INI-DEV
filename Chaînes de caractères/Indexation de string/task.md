## Indexation de string

Voua pouvez accéder à un caractère d'une string si vous connaissez sa position.
Par exemple, `str[index]` vous fournira le caractère à la position `index` dans la string `str`.
Notez que l'indexation commence toujours par `0`.
Une erreur `ValueError` sera levée s'il n'y a pas de caractère à l'index fourni.

Les index peuvent également être des nombres négatifs si vous voulez comptez depuis la droite (donc depuis la fin de votre string).
Notez que comme `-0` est égal à `0`, les index négatifs commence à partir de `-1`.

### Tâche
Utilisez l'indexation pour récupérer la lettre `'P'` à partir de `"Python"`.

<div class="hint">Pour rappel, les index commencent à partir de 0.</div>
