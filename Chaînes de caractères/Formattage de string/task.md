## Formattage de string

L'opérateur `%` après une string est utilisé pour la combiner avec des variables.

L'opérateur `%` va remplacer `%s` dans une string avec la valeur de la variable qui sera après.

Le symbole spécial `%d` est utilisé pour les valeurs entières ou décimales.  

> <i><b>Note</b>: Les opérations de formatage décrites ici présentent une variété de bizarreries 
> qui conduisent à un certain nombre d'erreurs courantes. 
> En utilisant les nouvelles chaînes formatées (voir [plus loin](course://Textes/F-strings)), 
> La méthode <code><a href="https://docs.python.org/3/library/stdtypes.html#str.format">str.format()</a></code> 
> , ou les <a href="https://docs.python.org/3/library/string.html#template-strings">modèles</a> peuvent aider à éviter ces erreurs. 
> Chacune de ces alternatives offre ses propres compromis et avantages de simplicité,
> de flexibilité et/ou d'extensibilité.</i>

### Tâche
Dîtes à PyCharm quel âge vous avez (en utilisant des chiffres).

<div class='hint'>Utilisez le symbole spécial <code>%d</code>.</div>
<div class='hint'>Quel âge avez-vous ?</div>
