##  Importation avec le mot clé from

Une forme d'importation permet l'importation direct d'un module via le mot clé `from`. Avec cette méthode, vous pouvez 
utilisez une fonction sans utiliser le nom du module `module_name`. Par exemple:
refix.  For example:

```python
from calculator import Add

calc = Add()    # name `Add` used directly without prefix `calculator`
```

Cela n'introduit pas le nom du module à partir duquel les importations sont faite dans la table des symboles locale
(donc dans notre exemple, `calculator` n'est pas défini).

Il existe même une option pour importer tous les noms définis par un module :
```python
from calculator import *
calc = Multiply()
```
Cela importe tous les noms sauf ceux commençant par un trait de soulignement `_`.
Dans la plupart des cas, les programmeurs Python ne l'utilisent pas, car cela introduit
un ensemble inconnu de noms dans l'interpréteur.

Si le nom du module est suivi de `as`, alors le nom suivant `as` est lié
directement au module importé :

```python
import my_module as mm
mm.hello_world()
```
Cela importe effectivement le module de la même manière que `import my_module`
le fait, à la seule différence qu'il est disponible via "mm". Il peut également être utilisé
lors de l'utilisation de "from" avec des effets similaires :


```python
from calculator import Subtract as Minus
```
Importez la classe `Calculator` à partir de `calculator` et créez une instance de cette classe.
Rappelez-vous comment y accéder correctement dans ce cas.

<div class="hint">Remarque : La classe <code>Calculator</code> doit être appelée sans préfixe car vous
l'importé directement.</div>

