altura = float(input("Digite a altura por favor: "))
peso = float(input("Agora digite seu peso: "))
imc = peso / (altura*altura)

if imc <= 15.9:
    print("Tão magro que virou osso")
elif imc <= 16.9:
    print("Muito abaixo do peso")
elif imc <= 18.4:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Acima do peso")
elif imc <= 34.9:
    print("Obesidade Grau I")
elif imc <= 40:
    print("Obesidade Grau II")
elif imc > 40:
    print("Obesidade Grau III")
else:
    print("Tente novamente, pode ter ocorrido um erro, sinto muito, estou melhorando aos poucos")

print("Seu IMC é: %.4f" % imc,"Kg")