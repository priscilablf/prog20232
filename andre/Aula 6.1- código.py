tempoExperimento = 1 #s
frequenciaSensor = 10 #Hz
qtDados = tempoExperimento * frequenciaSensor
#coleta
dado = []
for contador in range(qtDados):
    dado.append(float(input()))


#dado = [89127, 1298, 902, 3097, 356]
#soma = dado[0] + dado[1] + dado[2] + dado[3]
#print(soma)

soma = 0
for contador in range(len(dado)):
   soma = soma + (1/frequenciaSensor) * dado[contador]
print(soma)