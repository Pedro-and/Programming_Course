def calcular_imposto(salario):
    if salario <= 2259.20:
        aliquota = 0
        parcela = 0
    elif 2259.21 <= salario <= 2826.65:
        aliquota = 0.075
        parcela = 169.44
    elif 2826.66 <= salario <= 3751.05:
        aliquota = 0.15
        parcela = 381.44
    elif 3751.06 <= salario <= 4664.68:
        aliquota = 0.225
        parcela = 662.77
    elif salario > 4664.68:
        aliquota = 0.275
        parcela = 896.00
    imposto = (salario * aliquota) - parcela
    return imposto

salario = float(input("Digite seu salario: "))
imposto = calcular_imposto(salario)
print(imposto)