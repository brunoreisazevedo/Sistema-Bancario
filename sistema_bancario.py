def fsacar(*,saldo, limite,numero_saques, extrato,):
    valor = float(input("Informe o valor do saque: "))
   
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, numero_saques, extrato


def fdepositar(saldo, extrato,/):
        
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato


def fextrato(*,extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        return saldo


def fcadastar_cliente (cpf):
     global CLIENTES
     sair = False

     while True:
        if not sair:
            nome = input("Digite o nome do cliente: ")
            if len(nome) > 0 and nome != "exit":
                while True:
                    if not sair:
                        dt_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
                    else: break

                    if len(dt_nascimento) == 10 and dt_nascimento != "exit" and sair == False:
                        while True:
                            endereco = input("Digite a data de nascimento (Logradouro, número - Bairro - Cidade/UF): ")
                            if len(endereco) > 10 and endereco != "exit":
                                CLIENTES[cpf] = {"nome":nome, "dt_nascimento":dt_nascimento, "endereco":endereco}
                                print(f"Cliente {nome} de CPF {cpf} foi cadastrado com sucesso.")
                                sair = True
                                break
                            elif endereco == "exit":
                                sair = True
                                break

                    elif dt_nascimento == "exit":
                        sair = True
                        break

            elif nome == "exit":
                sair = True
                break

        else: break
     

def flista_clientes(tipo):
    
    if tipo == "T":
        for chave, valor in CLIENTES.items():
            print(chave, valor)
    else: 
        if tipo == "P":
            for chave, valor in CLIENTES.items():
                print(chave, valor["nome"])



def fcadastrar_conta(cpf):
    global CONTAS
    conta = list(CONTAS.keys())[-1]
    conta += conta
    CONTAS [conta] = {"agencia":"0001", "cpf":cpf}
    print(f"A conta {conta} foi cadastrada para o CPF {cpf}")


def flista_contas():
    for chave, valor in CONTAS.items():
        print(chave, valor)




menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[1] Cadastrar Cliente
[2] Listar Clientes
[4] Cadastrar Conta
[5] listar Conta
[q] Sair

=> """

CONTAS = {
    1:{"agencia":"0001", "cpf":"10010002002"}
}

CLIENTES = {
    "10010002002":{"nome":"Maria", "dt_nascimento":"15/02/2002", "endereco":"Rua Maranhão, 166 - Funcionários - Belo Horizonte/MG"},
    "10020001990":{"nome":"Marta", "dt_nascimento":"09/04/1990", "endereco":"Rua Aimores, 604 - Funcionários - Belo Horizonte/MG"},
}

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = fdepositar(saldo, extrato)

    elif opcao == "s":
        saldo, numero_saques, extrato = fsacar( saldo=saldo, limite=limite, numero_saques=numero_saques, extrato=extrato )
        
    elif opcao == "e":
        saldo = fextrato(extrato=extrato)
    
    elif opcao == "1":
        cpf = input("Informe o CPF (11 digitos): ")

        if len(cpf) == 11 and cpf.isdigit():
            if cpf in CLIENTES:
                print(f"Cliente com CPF {cpf} já cadastrado.")
            else:
                fcadastar_cliente(cpf=cpf)
        else:
            print(f"O CPF '{cpf}' está com valor incorreto")

    elif opcao == "2":
        flista_clientes("T")

    elif opcao == "4":
        flista_clientes("P")
        cpf = input("Digite o CPF de um dos clientes: ")
        if len(cpf) == 11 and cpf.isdigit():
            if cpf in CLIENTES:
                fcadastrar_conta(cpf=cpf)
            else:
                print("CPF não cadastrado. Selecione um CPF da lista de de clientes.")

    elif opcao == "5":
        flista_contas()    

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")