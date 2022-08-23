## Les modules incluent dans Python 
Python est fourni avec une [bibliothèque standard de module](https://docs.python.org/3/library/).

Certains modules sont intégrés dans l'interpréteur ; ceux-ci donnent accès à des opérations qui
ne font pas partie du noyau du langage, mais sont néanmoins intégrés, soit pour l'efficacité
ou pour fournir un accès aux primitives du système d'exploitation, telles que les appels système.
Un module particulier mérite une certaine attention : `sys`, qui est intégré dans chaque interpréteur Python.
Les variables `sys.ps1` et `sys.ps2` définissent les chaînes utilisées comme primaire et
invites secondaires si l'interpréteur est en mode interactif :
```text
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
```

La variable `sys.path` est une liste de chaînes qui détermine le chemin de recherche de l'interpréteur
pour les modules : voyez ce qu'il affiche pour vous lorsque vous l'exécutez.

N'oubliez pas que vous pouvez utiliser la complétion de code après un point (.) pour explorer les méthodes disponible 
d'un module. Vous pouvez en savoir plus sur les modules standards <a href="https://docs.python.org/3/tutorial/modules.html#standard-modules">ici</a>.
  
Imprimez la date actuelle à l'aide d'un module intégré `datetime`.
 
<div class='hint'>Utilisez la fonction <code>datetime.datetime.today()</code>.</div>
