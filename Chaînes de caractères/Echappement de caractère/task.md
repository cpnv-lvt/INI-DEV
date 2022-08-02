## Echappement de caractère

Le backslash est utilisé pour échapper les symboles spéciaux, tels qu'un apostrophe ou un guillemet,
par exemple, `"It\'s me"` ou `"She said \"Hello\""`. 

Si vous voulez effectivement écrire le caractère <code>\\</code> dans une chaîne de caractère,
vous devrez l'échapper également. Par exemple, voici comment afficher un backslash :

```python
print('\\')
```

Le symbole spécial `'\n'` est utilisé pour ajouter un retour à la ligne dans une string, 
alors que `'\t'` sert pour une tabulation.

Les caractères de citation ont une signification spéciale dans le code et peuvent donc être échappés également avec un backslash.
Si vous voulez mettre un des deux dans une string, vous pouvez aussi utiliser l'autre pour englober la chaîne de caractère,
sans besoin de caractère d'échappement.
Un apostrophe n'a pas besoin d'être échapper dans une string entourée de guillemets et inversement.
D'ailleurs, nous vous conseillons de choisir votre préféré entre l'apostrophe et le guillemet et d'utiliser,
de manière constante, votre choix.

Vous pouvez en apprendre plus sur le sujet <a href="https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals">ici</a>.  

### Tâche
Affichez le texte suivi en utilisant une seule string :
```text
The name of this ice cream is "Sweet'n'Tasty"  
```


<div class='hint'>Utilisez le backslash pour échapper les caractères de citation.</div>
