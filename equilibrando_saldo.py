
def equilibrar_saldo():
     saldo = 0 
     saldo_atual = float(input())
     valor_deposito = float(input())
     valor_retirada = float(input())
     saldo += saldo_atual + valor_deposito - valor_retirada
     print(f'O saldo final é:R$ {saldo:.1f}')

equilibrar_saldo()
