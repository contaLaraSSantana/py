#Zé Pescador precisa de um sistema simples para registrar o peso (em gramas) e o preço por quilo
#de um peixe. Crie um programa que permita a entrada do peso em gramas, converta-o para quilos,
#e calcule o valor total da venda. Em seguida, exiba o valor na saída.

peso= float(input("Qual o peso (em gramas)?: "))
preco=float(input('Qual o preço por kg?: '))

quilo= peso/1000
valor= quilo*preco
print("O valor total da venda foi de:",valor)

