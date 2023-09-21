#Problema experimento com
#Coleta e processamento

#dados (entrada e saída)
#tempo?
# tempoExperimento = 1 #s
# frequenciaSensor = 10 #Hz

def coletarDados (tempoExperimento,frequenciaSensor):
    """
    Essa função fou feita para coletar dados de um sensor tendo como entrada o tempo de experimento e a frequencia de sensor
    """
    qtDados = tempoExperimento * frequenciaSensor
    # coleta
    dado = []
    for contador in range(qtDados):
        dado.append(float(input()))
    return dado  #tudo isso é memória, do def ao dado

def integrar (dado,frequenciaSensor):
    soma = 0
    for data in dado:
        soma = soma + (1/ frequenciaSensor) * data
    return soma

#dados = coletarDados (1,10) 
#isso é processamento, a execução começa aqui. Executando o que está aí dentro na sequência.

tempo = 1
freq = 1
dadosEx1 = coletarDados (tempo, freq)
integral = integrar(dadosEx1, freq) #o processamento está acontecendo 



# dadosEx2 = coletarDados (1,2)
# dadosEx3 = coletarDados (1,10)







