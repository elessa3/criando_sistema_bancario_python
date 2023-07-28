# Sistema Bancario

menu = """

[D] Deposito
[S] Saque
[E] Extrato
[X] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:
    opcao = input(menu)

    # INICIO DEPOSITO
    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido! Tente novamente!")
        # FIM DEPOSITO

        # INICIO SAQUE*******
    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        # tratamento de excessoes

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques

        if excedeu_saldo:
            print("Saldo insuficiente! \nOperação não realizada")
        elif excedeu_limite:
            print("Limite excedido! Tente novamente! \nOperação não realizada!")
        elif excedeu_saques:
            print("Limite de saques diários excedido! \nOperação não realizada")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido! \nOperação não realizada")

        # FIM SAQUE*******

    elif opcao == "E":
        print("\n********** Extrato **********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n*****************************")

    elif opcao == "X":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
