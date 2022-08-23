## Méthodes de dictionnaire

Il y a plusieurs méthodes très utiles pour les dictionnaires, comme `keys()`,  `values()`, et `items()`.

La méthode `keys()` retourne une vue qui affiche une liste de toutes les clés du dictionnaire dans l'ordre d'insertion.

La méthode `values()` retourne une nouvelle des valeurs du dictionnaire.

Quand la méthode `items()` est appelée, elle retourne une vue du dictionnaire sous forme de tuples dans une liste
(paires de `(clef, valeur)`).

Les objets retournés par les méthodes `dict.keys()`, `dict.values()`,
et `dict.items()` fournissent une vue dynamique sur les entrées du dictionnaire,
c'est-à-dire que lorsque le dictionnaire change, la vue reflète ces changements.

Vous pouvez découvrir le reste des méthodes en utilisant &shortcut:CodeCompletion;
après le nom du dictionnaire suivi par un point.

Vous pouvez en apprendre plus sur les opérations sur les dictionnaires
<a href="https://docs.python.org/3/library/stdtypes.html#typesmapping">ici</a>.

### Tâche
Affichez toutes les valeurs de `phone_book`.

<div class='hint'>Utilisez la méthode <code>values()</code>.</div>
