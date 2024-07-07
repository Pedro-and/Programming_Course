height = float(input("Digite sua altura: "))
weight = float(input("Digite seu peso: "))
imc = weight / (height**2)

while(height <= 0.6 or height >= 2.5):
    print("Digite uma altura válida entre 0,6 metros e 2,5 metros")
    height = float(input())
while(weight <= 15 or weight >= 250):
    print("Digite um peso válido entre 15kg e 250kg")
    weight = float(input())
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9 :
    print("Peso normal")
elif 25 <= imc <= 29:
    print("Sobrepeso")
elif 30 <= imc <= 34.5:
    print("Obesidade grau I")
elif 35 <= imc <= 39.9:
    print("Obesidade grau II")
elif imc > 40:
    print("Obesidade grau III")
print(float(f"{imc:.2f}"))
