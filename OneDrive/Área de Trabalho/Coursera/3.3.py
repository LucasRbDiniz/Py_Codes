score = input("Enter score: ")
ponto = float(score)
if ponto > 1.0 or ponto < 0.0:
    print("Pontuação não válida")
    quit()
elif ponto >= 0.9:
    print("A")
elif ponto >= 0.8:
    print("B")
elif ponto >= 0.7:
    print("C")
elif ponto >= 0.6:
    print("D")
elif ponto < 0.6:
    print("F")
