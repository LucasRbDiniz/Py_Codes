palavra = input("Digite a palavra: ")
char = input("Qual char deseja contar?: ")
contagem = 0
for letra in palavra:
    if letra == char:
        contagem = contagem + 1
print(contagem)
