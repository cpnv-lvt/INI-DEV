## L'exécution de module en tant que script

Un module Python est un fichier contenant des instructions exécutables ainsi que des définitions de fonctions
ou de classes. Ces instructions sont exécutées la première fois que le nom du module est rencontré 
dans une instruction `import`. Le nom du fichier est le nom du module avec le suffixe .py ajouté. 
Au sein d'un module, le nom du module (sous forme de chaîne) est disponible en tant que valeur de la variable globale
`__name__`.


Lorsque vous exécutez un module **directement** (c'est-à-dire sans l'importer dans un autre),
le code du module sera exécuté, comme si vous l'aviez importé, mais avec
`__name__` défini sur `"__main__"`.

Vous pouvez utiliser `__name__` et `__main__` comme:

```python
if __name__ == "__main__":
   #faire quelque chose ici
```
Les instructions à l'intérieur de ce bloc ne seront exécutées que si le module est exécuté directement 
et non par importation depuis un autre module. Par exemple, considérons deux fichiers :

programme_principal :
```python
import some_module

print(f"main_program __name__ is: {__name__}")

if __name__ == "__main__":
   print("main_program executed directly")
else:
   print("main_program executed when imported")
```

some_module:
```python
print(f"some_module __name__ is: {__name__}")

if __name__ == "__main__":
   print("some_module executed directly")
else:
   print("some_module executed when imported")
```

Sortie après l'exécution de `main_program`:
```text
some_module __name__ is: some_module
some_module executed when imported
main_program __name__ is: __main__
main_program executed directly
```

Sortie après l'exécution de `some_module`:
```text
some_module __name__ is: __main__
some_module executed directly
```
## task
modifiez `task.py` et `some_module.py` de tel manière que si vous exécuter task.py, la sortie sera la suivante :

```text
This is a message from some_module.
This is a message from __main__.
This is a message from the function in the imported module.
This should be printed ONLY when task.py is called directly.
```
