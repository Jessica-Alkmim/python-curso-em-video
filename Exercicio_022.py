from itertools import count


nome = str(input('Digite seu nome completo:')).strip()

print ('Analisando seu nome...')
print (f'Seu nome em maiúsculo é {nome.upper()}')
print (f'Seu nome em minúsculo é {nome.lower()}')
print (f"Seu nome tem ao todo {len(nome)-nome.count(' ')} letras")
print ('Seu primeniro nome é  e ele tem  lestras')