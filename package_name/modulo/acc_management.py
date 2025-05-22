def cadastrar_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com o CPF informado!")
        return
    
    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a Data de Nascimento: ")
    endereco = input("Informe o endereço (logradouro, número, bairro, sigla da cidade/sigla do estado): ")

    usuarios.append({"nome" : nome, "nascimento" : nascimento, "cpf": cpf, "endereco" : endereco})

    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada para o usuário informado!")
        print(f"Agência: {agencia} - Conta: {numero_conta}")
        
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    # else:
    print("\nUsuário não cadastrado. Por favor cadastre um usuário.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Titular: {conta['usuario']['nome']}
            Agência: {conta['agencia']} - Conta: {conta['numero_conta']}
        """
    print(linha)
