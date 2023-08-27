# informacaoDoTeclado= int(input()) #neuroengenharia
# print(informacaoDoTeclado+2) #mestrado

peso = float(input('Digite o seu peso (kg): ')) 
altura = float(input('Digite a sua altura (m): '))
imc = peso/(altura**2)
print("Seu IMC é:", imc)
# print("estou muito abaixo do peso?", imc<17)
# print("estou abaixo do peso?", imc>=17 and imc <18.5)
# print("estou no peso normal?", imc >=18.5 and imc <25)
# print("estou acima do peso normal?", imc >=25 and imc <30)
# print("estou muito acima do peso normal?", imc >30)

if imc<17:
    print("estou muito abaixo do peso!")
elif imc>=17 and imc <18.5:
    print("estou abaixo do peso!")
elif imc >=18.5 and imc <25:
    print("estou no peso normal!")
elif  imc >=25 and imc <30:
    print("estou acima do peso normal")
else:
    print("estou muito acima do peso!")
    