
from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto:'))
cateto_adijacente = float(input('Comprimento do cateto adijacente :'))

hi = hypot(cateto_oposto, cateto_adijacente)

print  (f'A hipotenusa vai medir {hi:.2f}')