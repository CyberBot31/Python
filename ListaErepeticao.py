print('\t ----Cálculo do novo salário ---- ')
QuantProf = int(input('Quantidade de professores: '))
salarios = []
salariosCabonoG = []
salariosCabonoM = []
num = 1;
soma = 0.0
while num <= QuantProf:
    print('Informe o salario atual: ')
    salario_atual = float(input());
    salarios.append(salario_atual)
    num +=1

    if (salario_atual < 1000):
        salario_novo = salario_atual+245 
        salariosCabonoM.append(salario_novo)
        gastos1 = salario_novo - salario_atual

    elif (salario_atual >= 1000):
        salario_novo2= salario_atual + salario_atual*0.245
        salariosCabonoG.append(salario_novo2)
        gastos2 = salario_novo2 - salario_atual

    else:
        print('Salario sem bônus', salario_novo)
        
Total = gastos1 + gastos2

print('Quantidade de professores:',QuantProf,'\n', 'Salario inicial:',salarios,'\n',
      'Salario com abono Máximo: ',salariosCabonoG,'\n', 'Salario com abono Minímo:', salariosCabonoM,'\n', 'Gastos com abono: ',Total)