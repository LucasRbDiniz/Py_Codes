bign = 0
lown = None
while True:
    valor = input("Enter a number: ")
    if valor == 'done':
        break
    try:
        ivalor = int(valor)
    except:
        print('Invalid input')
        continue
    if ivalor > bign:
        bign = ivalor
    if lown is None:
        lown = ivalor
    elif ivalor < lown:
        lown = ivalor
print('Maximum is', bign)
print('Minimum is', lown)