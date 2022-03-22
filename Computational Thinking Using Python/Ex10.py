# . Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
# Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
# seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos.


metrosS = float(input("Digite a distância em metros: "))
tempoS = float(input("Digite o tempo em segundos: "))



result = metrosS / tempoS
print("==================================================================");
print("A media em metros por segundos: ", round(result,2))
print("==================================================================");
