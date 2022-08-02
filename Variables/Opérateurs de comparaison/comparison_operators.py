one = 1
two = 2
three = 3

# Cette opération enchaînée signifie que (one < two) et que (two < three)
# les comparaisons sont effectuées en même temps.
print(f"one < two < three: {one < two < three}")

# Insérez n'importe quel opérateur rendant l'expression véridique. Il y a plusieurs options.
is_greater = three ? two
print(f"three is greater than two: {is_greater}")

# Insérez n'importe quel opérateur rendant l'expression véridique. Il y a plusieurs options.
is_less = one ? three
print(f"one is smaller than three: {is_greater}")

# Insérez n'importe quel opérateur rendant l'expression véridique. Il y a plusieurs options.
is_true = one ? three ? two
print(f"one is smaller than three, which is greater than two: {is_true}")

# Insérez n'importe quel opérateur rendant l'expression véridique. Il y a plusieurs options.
not_equal = one ? two
print(f"one does not equal two: {not_equal}")

# Insérez n'importe quel opérateur rendant l'expression véridique. Il y a plusieurs options.
is_equal = three ? three
print(f"three equals three : {is_equal}")
