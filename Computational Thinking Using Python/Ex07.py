# Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
# dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
# divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão



num = int(input("Digite um numero de 0 a 99: "));


while num < 0 or num > 100:
    
    num = int(input("Você tem que digitar o numero com range de [0 até 99] tente novamente: "));

else:   
    print("========================================")
    if num < 10:
        print("Dezena(s): N/A - Não tem dezena")
        print("Unidade(s):", num)
        print("========================================")
       
    else:
        num = str(num)
        print("========================================")
        print("Dezena(s):", num[0])
        print("Unidade(s):", num[1])
        print("========================================")
    

        
