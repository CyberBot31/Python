numero = int(input("Insira o número: "))
numero = str(numero)

vetor_A = []

for y in numero:
    vetor_A.append(y)
    
print(vetor_A[::-1])