# Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual
# de aumento. Você deverá escrever um algoritmo que recebe 2 números reais representando
# os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que
# João obteve.


salarioA = float(input("Digite seu sálario anterior: "))
salarioB = float(input("Digite seu sálario reajustado: "))


result = (salarioB - salarioA);
result = (result / salarioA) * 100;


print("==============================================================");
print("O seu sálario aumentou em", round(result,2) , "%");
print("==============================================================");