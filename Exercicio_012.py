from operator import indexOf


produto = float(input('Qual é o preço de produto? R$'))

print(f'O produto que custava R${produto} com desconto de 5% vai custar R${produto - (produto*0.05):.2f}')