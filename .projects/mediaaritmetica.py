mediaAnual = 24

bimestre1 = float(input('Insira a nota do primeiro bimestre: '))
bimestre2 = float(input('Insira a nota do segundo bimestre: '))
bimestre3 = float(input('Insira a nota do terceiro bimestre: '))
bimestre4 = float(input('Insira a nota do quarto bimestre: '))

notasBimestrais = bimestre1 + bimestre2 + bimestre3 + bimestre4
mediaFinal = notasBimestrais / 4
quantoPrecisaParaPassarDeAno = mediaAnual - notasBimestrais

if mediaAnual <= 24:
    print(f"Sua media anual foi de {mediaFinal}, e você precisa de {quantoPrecisaParaPassarDeAno} para ser aprovado")
