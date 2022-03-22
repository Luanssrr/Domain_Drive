# Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
# um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
# deverá ler o número de camisas, o número de calças e o número de pares de sapato.


camisas = int(input("Digite a quantidade de camisas: "));
calcas = int(input("Digite a quantidade calças: "));
sapatos = int(input("Digite a quantidade pares de sapatos: "));


manDif = camisas * calcas * sapatos;

print("===============================================================================================");
print("A Quantidade de combinações possiveis de você se vestir é: ", manDif , "combinações");
print("===============================================================================================");