## Types de variable

Toutes les données dans un programme en python sont représentées par des objets ou des relations entre des objets.
Chaque objet a une identité, un type et une valeur.
L'identité d'un objet ne changera jamais après sa création, nous pouvons la considérer comme son adresse dans la mémoire.

Le `type` d'un objet détermine les opérations qu'il va supporter (p.e. "Est-ce qu'il a une longueur définie")
et va également définir les valeurs possible pour ce type d'objet.
La fonction `type()` retourne le type de l'objet (le type étant un objet lui-même).
Tout comme son identité, le type d'un objet ne pourra pas changer après sa création.

La valeur de certains objets peut changer. Les objets pour lesquels la valeur peut être modifiée sont <i>variables</i>;
Les objets dont la veleur ne peut être changée sont <i>immuables</i>, cela signifie que leur valeur est constante.

En Python, il y a deux types principaux pour les nombres: integers et floats.
La plus grande différence entre eux est qu'un `float` est un nombre décimal (à virgule),
alors qu'un `int` est un nombre entier (sans virgule).

Pour plius d'informations sur le sujet, aller dans les sections "<a href="https://docs.python.org/3/reference/datamodel.html#objects-values-and-types">Objects, values and types</a>"
et "<a href="https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy">The standard type hierarchy</a>"
dans la documentation Python.

### Tâche
Affichez le type de la variable `float_number`.

<div class="hint">
Regardez comment nous déterminons le type de la variable <code>number</code> à la ligne 2 et faîtes la même chose avec <code>float_number</code>.</div>
