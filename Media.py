notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calcular a media
mediafinal = (notaA + notaB) /2

#verificacao
if mediafinal > 7.0:
    print("A media %.1f - Aprovado"% mediafinal)
elif  mediafinal == 7.0:
    print("A media %.1f - Passou em cima da media" % mediafinal)
else:
    print("A media %.1f - Reprovado" % mediafinal)