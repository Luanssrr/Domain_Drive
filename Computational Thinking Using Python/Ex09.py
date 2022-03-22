# Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula
# e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés
# de um desconto, fosse um aumento. O que muda no seu algoritmo?


print("=============== C A L C U L A D O R A - D E S C O N T O ===============")


print("Descontar% Opção [1]")
print("Aumentar%  Opção [2]")
desc = int(input("Escolha a opção: "));
print("=======================================================================");

if desc == 1:
    valor = float(input("Digite o preço do produto que quer aplicar o desconto : "))
    taxa = float(input("Digite o (%) de desconto: "))
    total = (valor * taxa) / 100;
    total -= valor;
else:
    valor = float(input("Digite o preço do produto que quer aplicar o desconto : "))
    taxa = float(input("Digite o (%) de desconto: "))
    total = (valor * taxa) / 100;
    total += valor;
      
    
    print("====================================================================");
    print("valor final:", valor)
    print("====================================================================");



