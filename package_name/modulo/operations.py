from datetime import date, datetime

def consulta_saldo(saldo):
    print(f"\nSaldo:         R$ {saldo:.2f}")

def consulta_extrato(saldo, /, *, extrato):
    print("\n***************** EXTRATO *****************")
    print(extrato if extrato else "Não foram realizadas operações.")
    print("\n*******************************************")
    print(f"Saldo:         R$ {saldo:.2f}")
    print("\n*******************************************")

def sacar(*, saldo, valor, extrato, limite_saque, numero_saques, saques_diarios):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    
    saldo_excedido = valor > saldo #
    limite_excedido = valor > limite_saque #
    saques_exedidos = numero_saques >= saques_diarios #

    if saques_exedidos:
        print("\nLimite de saques diários excedidos.")

    elif valor < 0:
        print("Valor informado inválido para a operação.")
    
    elif limite_excedido:
        print(f"\nLimite de saque excedido para a operação. (Limite atual: R$ {limite_saque:.2f})")
    
    elif saldo_excedido:
        print(f"\nSaldo insuficiente para a operação. Saldo atual: R$ {saldo}")

    else:
        saldo -= valor
        numero_saques += 1

        hora = datetime.now()
        extrato += f"{hora.strftime(mascara_ptbr)} - Saque:         R$ {valor:.2f}\n" # Registra extrato

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    
    if valor > 0:
        saldo += valor

        hora = datetime.now()
        extrato += f"{hora.strftime(mascara_ptbr)} - Depósito:      R$ {valor:.2f}\n" # Registra extrato

        print("Depósito realizado com sucesso!")

    else:
        print("Valor informado inválido para a operação.")

    return saldo, extrato


