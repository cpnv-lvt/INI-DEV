def func():
    print('This is a message from the function in the imported module.')


print(f'This is a message from {__name__}.')

# Faite un changement ici.
print('This should not be printed')

