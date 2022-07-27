## Commentaires

Les commentaires en Python commencent par le caractère dièse (`#`) suivi d'un espace, 
cela sera valable pour la suite entière de la ligne. 
Vous pouvez également utiliser &shortcut:CommentByLineComment; 
pour commenter ou décommenter une ligne ou même un block de code dans PyCharm.


N'oubliez pas de maintenir vos commentaires à jour au fur et à mesure de l'évolution du code !
Les commentaires qui contredisent le code sont encore pire que l'absence de commentaires.
Veillez également à faire des commentaires pertinents. Il est inutile de commenter des lignes qui sont claires par elles-mêmes, 
de plus, afin de faciliter la maintenance des commentaires, 
veillez à éviter de placer vos commentaires en suite de ligne, comme ça :


```python
x = x + 1                 # Incrémente x
```

Les commentaires doivent être des phrases complètes. 
Faîtes en sorte que vos commentaires soient clairs et faciles à comprendre pour d'autres personnes.


#### Block de commentaires

Les blocks de commentaires sont là pour faciliter la compréhension du code qui soit et sont indentés comme le code lui-même.

#### Commentaires alignés
Bien que déconseillés, les commentaires faits sur la même ligne que du code doivent être séparés du code d'au moins deux espaces.
Attention, les commentaires alignés peuvent être comptés comme des erreurs par certains enseignants.


Pour plus d'informations sur la manière de commenter correctement, 
vous pouvez consulter les consignes du langage Python : <a href="https://www.python.org/dev/peps/pep-0008/#comments">PEP 8 – Style Guide for Python Code</a>. 
  
Vous pouvez également commenter une ligne ou un block de code si vous ne voulez pas le supprimer ou s'il sera utile par la suite. 
C'est également ce que nous conseillons afin de valoriser ce que vous auriez fait durant un test mais que vous n'auriez pas eu le temps de finir ou de corriger.

### Tâche
Dans l'éditeur de code, commentez la ligne avec la commande `print` qui indique qu'elle ne devrait pas être affichée.
Regardez la différence lors de l'exécution du code.

<div class="hint">
  Ajoutez un <code>#</code> et un espace avant la commande <code>print</code>. Laissez le reste tel qu'il est.
</div>
