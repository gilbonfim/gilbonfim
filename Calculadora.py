# Calculadora
res = 0
n1 = float(input("Primerio número: "))
ope = str(input("Digite a operação: ")).strip()[0]
n2 = float(input("Segundo número: "))
if ope[0] == '+':
    print(f'A soma de ', end='')
    res = n1 + n2
elif ope == '-':
    print(f'A subtração de ', end='')
    res = n1 - n2
elif ope == '*':
    print('A multiplicação de ', end='')
    res = n1 * n2
elif ope == '/':
    print('A divisão de ', end='')
    res = n1 / n2
else: 
    print('Operação não suportada.')

print(f'{n1} e {n2} é igual a {res}')
    