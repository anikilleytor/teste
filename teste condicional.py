PH = float(input('Digite um valor do PH: '))
if PH < 6.0:
    r = 'acido'
elif PH < 7.0:
    r = 'levemente acida'
elif PH == 7:
    r = 'neutra'
elif  PH < 8.0:
    r = 'levemente alcalina'
else:
    r = 'alcalino'
print(f'Com pH = {PH} a soluçao e {r}')
