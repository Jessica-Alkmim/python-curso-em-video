dias = int(input('Quantos dias alugados?'))
km = float(input('Quatos Km rodados?'))
aluguel = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${aluguel:.2f}')