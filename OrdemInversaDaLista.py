years = []
heights = []
for i in range(1, 6):
    print('%dº Pessoa' %i)
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    years.append(idade)
    heights.append(altura)

print('Ordem inversa')
print('Alturas')
print(heights[::-1])
print('Idades')
print(years[::-1])

print('Ordem lida')
print('Alturas')
print(heights)

print('Idades')
print(years) 