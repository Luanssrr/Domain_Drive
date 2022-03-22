# Uma disciplina da faculdade possui 3 tipos de avaliações: NAC, AM e PS. A média da
# disciplina é calculada de forma ponderada, onde a NAC tem peso 2, o AM peso 3 e a PS
# peso 5. Escreva um algoritmo que calcula a média da disciplina, seu algoritmo deverá receber
# as três notas (NAC, AM e PS) e deverá imprimir o valor da média.
# MEDIA = (2 ∗ NAC + 3 ∗ AM + 5 ∗ P S)/10

notaNAC = float(input("Digite sua nota NAC: "))
notaAM = float(input("Digite sua nota AM: "))
notaPS = float(input("Digite sua nota PS: "))



media = (2 * notaNAC + 3 * notaAM + 5 * notaPS) / 10;

print("======================================");
print("Sua nota total foi de:", round(media,2));
print("======================================");