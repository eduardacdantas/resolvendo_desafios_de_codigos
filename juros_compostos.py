#DESAFIO 4 - JUROS COMPOSTOS
def calcular_investimento():
    valor_inicial = float(input())
    taxa_juros = float(input())
    periodo = int(input())
    valor_final = valor_inicial * (1 + taxa_juros)**periodo
    valor_final = round(valor_final, 2)
    print("Valor final do investimento: R$", valor_final)
calcular_investimento()
