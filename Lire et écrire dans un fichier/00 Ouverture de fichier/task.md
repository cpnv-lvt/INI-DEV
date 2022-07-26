## Ouverture d'un fichier
Python intègre plusieurs fonctions pour l’ouverture, la lecture et l’écriture d’un fichier.

`open()` permet l’ouverture d’un fichier. La plupart du temps on l’utilise avec deux arguments tel que :
`open(nom_de_fichier, mode)`:

```python
f = open('mon_fichier.txt', 'w')
```

Le premier argument est une chaine de caractère contenant le nom de fichier. Le second argument est une autre chaine de caractère permettant 
de définir le mode d’ouverture tel que :

`'r'`  : ouverture en lecture seul  
`'w'` : ouverture en écriture (attention, si le fichier existe il sera écrasé)  
`'a'`  : ouverture en mode addition (le texte ajouté le sera en fin de fichier)  
`'r+'` : ouverture en mode lecture/écriture  

Il est conseillé d’utiliser la méthode d’ouverture avec `with` afin d’automatiser la fermeture du fichier. Voici un exemple d’utilisation :

```python
with open('mon_fichier.txt') as f:
    read_data = f.read()

# Nous pouvons vérifier que le fichier est bien fermé automatiquement
f.closed
```
```text
True
```
**Important**:  

Si vous n’utilisez pas la méthode d’ouverture avec le terme ‘with’,  vous devrez utiliser ‘f.close()’ pour fermer le fichier et libéré la mémoire 
et les ressources système. De plus, lorsque vous utiliser ‘f.close()’, vous n’aurez plus accès au contenu du fichier. 

Dans votre éditeur, ouvrez le fichier ‘input1.txt’ en mode lecture avec la méthode ‘with’. Vérifier le nom utiliser pour le fichier 
sur les lignes suivantes et utiliser-le. A la fin, femer le fichier de sortie `outfile` préalablement ouvert.

Après l'execution de votre code, vérifier le fichier de sortie présent de la vue du cours à côté des autres fichiers.

<div class="hint">Utiliser l'argument <code>r</code> de la commande <code>open()</code>,
pour jouer un peu avec les fichiers!</div>
