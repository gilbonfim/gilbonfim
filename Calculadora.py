# Calculadora
res = 0
n1 = float(input("Primerio número: "))
ope = str(input("Digite a operação: ")).strip()[0]
n2 = float(input("Segundo número: "))
if ope[0] == '+':
    res = n1 + n2
elif ope == '-':
    res = n1 - n2
elif ope == '*':
    res = n1 * n2
elif ope == '/':
    res = n1 / n2
else: 
    print('Operação não suportada.')

print(f'{n1} {ope} {n2} é igual a {res}')
print('Testando alteraçẽos')    
