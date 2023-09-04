def calcular_valor_total(peso, preco_por_quilo):
    peso_quilos = converter_gramas_para_quilo(peso)

    valor_total = peso_quilos * preco_por_quilo
    
    valor_total = round(valor_total, 2)
    
    return valor_total

def converter_gramas_para_quilo(peso_gramas):
    peso_quilos = peso_gramas / 1000.0

    return peso_quilos

# Exemplo de uso das funções
peso_em_gramas = 1250  
preco_por_quilo = 9.68 

valor_total = calcular_valor_total(peso_em_gramas, preco_por_quilo)
peso_em_quilos = converter_gramas_para_quilo(peso_em_gramas)

print('Peso em quilos:',peso_em_quilos, 'kg')
print('Valor total da venda: R$',valor_total)
