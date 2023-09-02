PRECO_QUILO_PEIXE=9.69
valor_de_peixes_vendidos = 0
valor_total=0

while True:
    p= int(input("Você deseja registrar uma venda? Digite 1 para sim e 0 para não: "))

    if p == 1:
        valor_de_peixes_vendidos = valor_de_peixes_vendidos+1
        peso= float(input("Qual o peso em gramas?: "))
        quilo= peso/1000
        valor= quilo*PRECO_QUILO_PEIXE
        valor_total = valor_total+valor
        print("O valor total dessa venda foi de:",valor)
    elif p == 0:
        print("Registro de vendas cancelado")
        print("A quantidade de peixes vendidos foi: ",valor_de_peixes_vendidos)
        print("O valor total da venda foi de:", valor_total)
        break