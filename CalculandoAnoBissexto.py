Years = int(input('Ano: '))
if (Years%4==0 and Years%100!=0) or (Years%400==0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')