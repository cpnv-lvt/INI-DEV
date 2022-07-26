## lecture de fichier

Pour lire un fichier, vous pouvez utiliser la commande `f.read(size)`, qui lira une certaine 
quantité de donnée et renvera une chaine de caractères. Lorsque la taille est omis ou négative, 
l'entier du fichier sera lu et retourner.

```python
with open('somefile.txt') as f:
    print(f.read())
```
```text
Here's everything that's in the file.\n
```
<i>**Note**: Il peut y avoir un problème si la taille du fichier fait deux fois la taille 
de la mémoire de votre ordinateur.</i>


`f.readline()` lit une seul ligne du fichier; un caractère de nouvelle ligne (`\n`) 
est laissé à la fin de la chaine. ce caractpre sera omi uniquement si vous êtes à la dernière ligne.
Si `f.readline()` retourne une chaine vide, la fin du fichier a été atteint, alors qu'une ligne vide 
sera représentée par `\n`, une chaine contenant uniquement le caractère de nouvelle line.

```python
f.readline()
```
```text
'This is the first line of the file.\n'
```
```python
f.readline()
```
```text
'Second line of the file\n'
```
```python
f.readline()
```
```text
''
``` 
For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and 
makes the code simple:
```python
for line in f:
    print(line)
```
```text
This is the first line of the file.
Second line of the file
```

If you want to read all the lines of a file in a list, you can also use `list(f)` or `f.readlines()`.


For more details, check out the section [Methods of File Objects](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) in Python Tutorial.


Print the contents of "input.txt" to output by iterating over the lines of the file and printing each one.
Then print only the first line of "input1.txt".

<div class="hint">Loop over the file object as in the example in the task description.</div>
<div class='hint'>Use the <code>print</code> function.</div>
<div class='hint'>Use the <code>readline()</code> method to print a single line.</div>
