nome = input("nome: ")
idade = int(input("digite sua idade"))

if idade > 65:
    print(nome + " é idoso e tem fila preferencial")
else:
    print(nome + " não é idoso e nao tem fila preferencial")