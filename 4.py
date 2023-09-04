class Venda:
    def __init__(self, peso_gramas, preco_por_quilo):
        self.peso_gramas = peso_gramas
        self.preco_por_quilo = preco_por_quilo
        self.valor_total = self.calcular_valor_total()

    def calcular_valor_total(self):
        peso_quilos = self.peso_gramas / 1000.0
        valor_total = peso_quilos * self.preco_por_quilo
        return round(valor_total, 2)

    def registrar_venda(self):
        with open("registro_vendas.txt", "a") as arquivo:
            arquivo.write("Peso em gramas:",self.peso_gramas)
            arquivo.write("Preço por quilo: R$",self.preco_por_quilo)
            arquivo.write("Valor total da venda: R$",self.valor_total)

# Exemplo de uso
peso_em_gramas = 1500
preco_por_quilo = 10  

venda = Venda(peso_em_gramas, preco_por_quilo)
venda.registrar_venda()
print("Venda registrada em 'registro_vendas.txt'.")
