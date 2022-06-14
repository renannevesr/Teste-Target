SP =67836.43
RJ =36678.66
MG =29229.88
ES =27165.48
Outros=19849.53

print("""
    1. SP
    2. RJ
    3. MG
    4. ES
    5. OUTROS
    """)
escolha = int(input("qual estado quer saber da comissão: "))
porcentagem = int(input("valor do percentual(sem o simbolo de %):"))
calc_porc = porcentagem/100
match escolha:
    case 1:
        calc = SP * calc_porc
        print("Valor da comissão de SP: ",calc)
    case 2:
        calc = RJ * calc_porc
        print("Valor da comissão de RJ: ",calc)
    case 3:
        calc = MG * calc_porc
        print("Valor da comissão de MG: ",calc)
    case 4:
        calc = ES * calc_porc
        print("Valor da comissão de ES: ",calc)
    case 5:
        calc = Outros * calc_porc
        print("Valor da comissão de Outros: ",calc)
