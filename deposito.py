#DESAFIO 5 - O GRANDE DEPÓSITO
valor = float(input())
if valor > 0:
    print(f"Deposito realizado com sucesso!\nSaldo atual: R$ {valor:.2f}")
elif valor == 0:
    print(f"Encerrando o programa...")
else:
    print(f"Valor invalido! Digite um valor maior que zero.")
