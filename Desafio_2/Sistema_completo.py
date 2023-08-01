# Sistema Bancario
import textwrap


def menu():
    menu = """\n
    -------------MENU-------------
    [D] Deposito
    [S] Saque
    [E] Extrato
    [NC] Nova Conta
    [LC] Listar Conta
    [NU] Novo Usuario
    [X] Sair
    =>"""
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n*** Depósito realizado com sucesso! ***")

    else:
        print("Valor inválido! Operação falhou!")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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
        print("\n*** Saque realizado com sucesso! ***")
    else:
        print("Valor inválido! \nOperação não realizada")

    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    print("\n********** Extrato **********")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n*****************************")
    return saldo, extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Ja existe usuário cadastrado com este CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = "Informe o endereço (logradouro, nro - bairro - cidade/UF):  "

    usuarios.append(
        {"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco}
    )

    print("** Usuário criado com sucesso! ***")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n*** Conta criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        # print('a' = 100)
        print(textwrap.dedent(linha))


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "E":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "X":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
