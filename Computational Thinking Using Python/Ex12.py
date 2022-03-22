# . O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
# recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
# o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5.
# Dica: realize várias divisões e restos de divisões por 10.
i = 0;
soma = 0;

rm = int(input("Digite seu RM[APENAS NUMERO]: "))

nova = str(rm) 
numeros = []   

while i < len(nova): 
    numeros.append(nova[i]); 
    soma += int(nova[i]);    
    i += 1;                                  
else:
   i = 1;
   print("======================================")
   print("Matricula : RM"+ nova)
   print("A soma do seu RM é:", soma,"=", nova[0], end="");
   while i < len(nova):
       print(" +", nova[i], end="");
       i += 1;   
       pass

       