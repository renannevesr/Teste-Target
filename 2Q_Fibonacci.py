
a,b =0,1
numero = int(input("Digite o número a ser consultado:"))
while a < numero:
    a, b = b, a+b
    if numero == a:
        print("O número informado pertence a sequência.")
if numero != a:
    print("O número informado não pertence a sequência.")