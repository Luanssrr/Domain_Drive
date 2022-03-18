# Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. Seu
# algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o m
# de 2022. Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu
# programa deverá imprimir:
# Fulano de tal tem (ou terá) 34 anos


nome = input("Digite seu nome: ")
anoN = int(input("Diite seu ano de nascimento: "))


anoA = 2022

print("Seu nome é", nome, "e você tem", (anoA - anoN), "anos")