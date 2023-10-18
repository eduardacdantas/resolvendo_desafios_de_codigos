#DESAFIO 2 - ORGANIZANDO SEUS ATIVOS

# Entrada dos códigos dos ativos
def organizar_ativos():
    ativos = []
    quantidadeAtivos = int(input())
    for _ in range(quantidadeAtivos):
        codigoAtivo = input()
        ativos.append(codigoAtivo)
        ativos = sorted(ativos)
    for ativo in ativos:
        print(ativo)
      
organizar_ativos()
