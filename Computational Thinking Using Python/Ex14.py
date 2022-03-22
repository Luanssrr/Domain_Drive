# As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento:
# à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário
# informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o
# desconto em percentual dado pela prefeitura para pagamento à vista.


iptu = float(input("Digite o valor do seu IPTU: "));

parc = (iptu / 10);
iptu -= (iptu * 0.03);





print("====================================================================");
print("Valor a vista do seu IPTU: R$" , round(iptu,3), "- Desconto de 3%");
print("Parcelamento em 10x: R$", parc);
print("====================================================================");