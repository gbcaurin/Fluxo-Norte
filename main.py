import os

#VARIAVEIS GLOBAIS

pedidos = {}
entregador = {}
contador_pedidos = 1
contador_entregadores = 1001
limite_pedidos = 5

#CADASTRO

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_id_pedido(id):
    if len(id) == 5 and id[0] == 'P' and id[1:].isdigit():
        return True
    return False

def validar_id_entregador(id):
    if len(id) == 4 and id.isdigit():
        return True
    return False

def gerar_id_pedido():
    global contador_pedidos
    id = f"P{contador_pedidos:04d}"
    contador_pedidos += 1
    return id

def gerar_id_entregador():
    global contador_entregadores
    id = str(contador_entregadores)
    contador_entregadores += 1
    return id

def cadastro_pedido():
    id = gerar_id_pedido()
    nome_cliente = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço de entrega: ")
    prioridade = input("Digite a prioridade do pedido (Alta ou Normal): ")

    prioridade = prioridade.lower()
    while prioridade not in ["alta", "normal"]:
        prioridade = input("Prioridade inválida. Digite 'Alta' ou 'Normal': ")
        prioridade = prioridade.lower()

    descricao = input("Digite a descrição do pedido: ")

    pedidos[id] = {"nome_cliente": nome_cliente, "endereco": endereco, "prioridade": prioridade, "descricao": descricao, "status": "Pendente", "entregador": None}
    print(f"Pedido cadastrado com ID: {id}")
    input("\n[Pressione Enter para continuar]")
    limpar_tela()

def cadastro_entregador():
    veiculos = ["carro", "van", "moto", "bicicleta", "patinete"]
    id = gerar_id_entregador()

    nome = input("Digite o nome do entregador: ")

    for id_entregador in entregador:
        if entregador[id_entregador]["nome"] == nome:
            print("Entregador já cadastrado.")
            input("\n[Pressione Enter para continuar]")
            limpar_tela()
            return

    veiculo = input("Digite o tipo de veículo: ")

    while veiculo.lower() not in veiculos:
        veiculo = input("Veículo inválido. Digite novamente: ")

    entregador[id] = {
        "nome": nome,
        "veiculo": veiculo,
        "pedidos": [],
        "status": True
    }

    print("Entregador cadastrado com ID:", id)
    input("\n[Pressione Enter para continuar]")
    limpar_tela()

#BUSCA

def buscar_pedido_por_id_interno(id_pedido):
    if id_pedido in pedidos:
        return pedidos[id_pedido]
    return None

def buscar_entregador_por_id_interno(id_entregador):
    if id_entregador in entregador:
        return entregador[id_entregador]
    return None

#EXIBICAO

def exibir_pedido(id_pedido, info):
    if info["entregador"] is None:
        id_ent = "Nao associado"
    else:
        id_ent = info["entregador"]
    print("-" * 50)
    print(f"ID: {id_pedido}")
    print(f"Cliente: {info['nome_cliente']}")
    print(f"Endereco: {info['endereco']}")
    print(f"Prioridade: {info['prioridade']}")
    print(f"Descricao: {info['descricao']}")
    print(f"Status: {info['status']}")
    print(f"Entregador: {id_ent}")

def exibir_entregador(id_entregador, info):
    if info["status"] == True:
        disponibilidade = "Disponivel"
    else:
        disponibilidade = "Indisponivel"
    print("-" * 50)
    print(f"ID: {id_entregador}")
    print(f"Nome: {info['nome']}")
    print(f"Veiculo: {info['veiculo']}")
    print(f"Disponibilidade: {disponibilidade}")

#ATUALIZACOES

def alterar_status_pedido():
    id_pedido = input("ID do pedido: ").strip().upper()

    if not validar_id_pedido(id_pedido):
        print("ID invalido.")
        return

    pedido = buscar_pedido_por_id_interno(id_pedido)
    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Cancelado":
        print("Pedido cancelado nao pode ser alterado.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao pode ser alterado.")
        return

    print("1-Pendente | 2-Em Rota | 3-Entregue")
    opcao = input("Novo status: ")

    if opcao == "1":
        novo = "Pendente"
    elif opcao == "2":
        novo = "Em Rota"
    elif opcao == "3":
        novo = "Entregue"
    else:
        print("Opcao invalida.")
        return

    if novo == "Em Rota" and pedido["entregador"] is None:
        print("Pedido sem entregador nao pode ir pra Em Rota.")
        return

    if novo == "Entregue" and pedido["status"] != "Em Rota":
        print("So entrega pedido que esta Em Rota.")
        return

    if novo == "Entregue":
        ent = buscar_entregador_por_id_interno(pedido["entregador"])
        if ent is not None and len(ent["pedidos"]) > 0:
            if ent["pedidos"][0] != id_pedido:
                print("Tem pedido mais antigo na fila, entregue ele primeiro.")
                return
            ent["pedidos"].remove(id_pedido)
            if len(ent["pedidos"]) < limite_pedidos:
                ent["status"] = True

    pedido["status"] = novo
    print("Status atualizado para:", novo)
    input("\n[Pressione Enter para continuar]")


def cancelar_pedido():
    id_pedido = input("ID do pedido: ").strip().upper()

    if not validar_id_pedido(id_pedido):
        print("ID invalido.")
        return

    pedido = buscar_pedido_por_id_interno(id_pedido)
    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Cancelado":
        print("Pedido ja esta cancelado.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao pode ser cancelado.")
        return

    if pedido["entregador"] is not None:
        ent = buscar_entregador_por_id_interno(pedido["entregador"])
        if ent is not None:
            if id_pedido in ent["pedidos"]:
                ent["pedidos"].remove(id_pedido)
            if len(ent["pedidos"]) < limite_pedidos:
                ent["status"] = True

    pedido["entregador"] = None
    pedido["status"] = "Cancelado"
    print("Pedido cancelado.")
    input("\n[Pressione Enter para continuar]")


def associar_entregador():
    id_pedido = input("ID do pedido: ").strip().upper()

    if not validar_id_pedido(id_pedido):
        print("ID invalido.")
        return

    pedido = buscar_pedido_por_id_interno(id_pedido)
    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Cancelado":
        print("Pedido cancelado nao recebe entregador.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao recebe entregador.")
        return

    if pedido["entregador"] is not None:
        print("Pedido ja tem entregador.")
        return

    id_entregador = input("ID do entregador: ").strip()

    if not validar_id_entregador(id_entregador):
        print("ID de entregador invalido.")
        return

    ent = buscar_entregador_por_id_interno(id_entregador)
    if ent is None:
        print("Entregador nao encontrado.")
        return

    if not ent["status"]:
        print("Entregador indisponivel.")
        return

    if len(ent["pedidos"]) >= limite_pedidos:
        print("Entregador atingiu o limite de", limite_pedidos, "pedidos.")
        return

    pedido["entregador"] = id_entregador
    pedido["status"] = "Em Rota"
    ent["pedidos"].append(id_pedido)

    if len(ent["pedidos"]) >= limite_pedidos:
        ent["status"] = False

    print("Entregador associado e pedido Em Rota.")
    input("\n[Pressione Enter para continuar]")


def remover_associacao():
    id_pedido = input("ID do pedido: ").strip().upper()

    if not validar_id_pedido(id_pedido):
        print("ID invalido.")
        return

    pedido = buscar_pedido_por_id_interno(id_pedido)
    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao pode desvincular.")
        return

    if pedido["entregador"] is None:
        print("Pedido nao tem entregador.")
        return

    ent = buscar_entregador_por_id_interno(pedido["entregador"])
    if ent is not None:
        if id_pedido in ent["pedidos"]:
            ent["pedidos"].remove(id_pedido)
        if len(ent["pedidos"]) < limite_pedidos:
            ent["status"] = True

    pedido["entregador"] = None
    pedido["status"] = "Pendente"
    print("Associacao removida, pedido voltou pra Pendente.")
    input("\n[Pressione Enter para continuar]")

#CONSULTAS

def pedidos_pendentes():
    print("\nPedidos Pendentes")
    encontrados = False
    for id_pedido, info in pedidos.items():
        if info["status"].lower() == "pendente":
            exibir_pedido(id_pedido, info)
            encontrados = True
    if not encontrados:
        print("Nenhum pedido pendente.")
    input("\n[Pressione Enter para continuar]")


def pedidos_em_rota():
    print("\nPedidos Em Rota")
    encontrados = False
    for id_pedido, info in pedidos.items():
        if info["status"].lower() == "em rota":
            exibir_pedido(id_pedido, info)
            encontrados = True
    if not encontrados:
        print("Nenhum pedido em rota.")
    input("\n[Pressione Enter para continuar]")


def pedidos_entregues():
    print("\nPedidos Entregues")
    encontrados = False
    for id_pedido, info in pedidos.items():
        if info["status"].lower() == "entregue":
            exibir_pedido(id_pedido, info)
            encontrados = True
    if not encontrados:
        print("Nenhum pedido entregue.")
    input("\n[Pressione Enter para continuar]")


def buscar_pedido_por_id():
    id_pedido = input("Digite o ID do pedido (ex: P0001): ").strip().upper()

    if not validar_id_pedido(id_pedido):
        print("ID de pedido invalido.")
        input("\n[Pressione Enter para continuar]")
        return

    pedido = buscar_pedido_por_id_interno(id_pedido)
    if pedido is None:
        print("Pedido nao encontrado.")
    else:
        exibir_pedido(id_pedido, pedido)
    input("\n[Pressione Enter para continuar]")


def entregadores_disponiveis():
    print("\nEntregadores Disponiveis")
    encontrados = False
    for id_entregador, info in entregador.items():
        if info["status"] == True:
            exibir_entregador(id_entregador, info)
            encontrados = True
    if not encontrados:
        print("Nenhum entregador disponivel.")
    input("\n[Pressione Enter para continuar]")


def buscar_entregador_por_id():
    id_entregador = input("Digite o ID do entregador: ").strip()

    if not validar_id_entregador(id_entregador):
        print("ID de entregador invalido.")
        input("\n[Pressione Enter para continuar]")
        return

    ent = buscar_entregador_por_id_interno(id_entregador)
    if ent is None:
        print("Entregador nao encontrado.")
    else:
        exibir_entregador(id_entregador, ent)
    input("\n[Pressione Enter para continuar]")


def entregas_realizadas_por_entregador():
    id_entregador = input("Digite o ID do entregador: ").strip()

    if not validar_id_entregador(id_entregador):
        print("ID de entregador invalido.")
        input("\n[Pressione Enter para continuar]")
        return

    ent = buscar_entregador_por_id_interno(id_entregador)
    if ent is None:
        print("Entregador nao encontrado.")
        input("\n[Pressione Enter para continuar]")
        return

    print(f"\nEntregas realizadas por {ent['nome']}")
    encontrados = False
    for id_pedido, info in pedidos.items():
        if info["status"].lower() == "entregue" and info["entregador"] == id_entregador:
            exibir_pedido(id_pedido, info)
            encontrados = True

    if not encontrados:
        print("Nenhuma entrega realizada por este entregador.")
    input("\n[Pressione Enter para continuar]")

#RELATORIOS

STATUS_VALIDOS = ["Pendente", "Em Rota", "Entregue", "Cancelado"]

def relatorio_total_pedidos():
    print("\nRelatorio - Total de Pedidos")
    print(f"Total de pedidos cadastrados: {len(pedidos)}")
    input("\n[Pressione Enter para continuar]")


def relatorio_pedidos_por_status():
    print("\nRelatorio - Quantidade de Pedidos por Status")
    for status in STATUS_VALIDOS:
        quantidade = 0
        for id_pedido in pedidos.keys():
            if pedidos[id_pedido]["status"].lower() == status.lower():
                quantidade += 1
        print(f"{status}: {quantidade}")
    input("\n[Pressione Enter para continuar]")


def relatorio_alta_prioridade():
    print("\nRelatorio - Pedidos com Alta Prioridade")
    encontrados = False
    for id_pedido in pedidos.keys():
        if pedidos[id_pedido]["prioridade"].lower() == "alta":
            exibir_pedido(id_pedido, pedidos[id_pedido])
            encontrados = True
    if not encontrados:
        print("Nenhum pedido de alta prioridade.")
    input("\n[Pressione Enter para continuar]")


def relatorio_entregador_maior_entregas():
    print("\nRelatorio - Entregador com Maior Numero de Entregas")

    if not entregador:
        print("Nenhum entregador cadastrado.")
        input("\n[Pressione Enter para continuar]")
        return

    totais = {}
    for id_ent in entregador.keys():
        totais[id_ent] = 0

    for id_pedido in pedidos.keys():
        id_ent = pedidos[id_pedido]["entregador"]
        if pedidos[id_pedido]["status"].lower() == "entregue" and id_ent in totais:
            totais[id_ent] += 1

    maior_id = max(totais, key=totais.get)
    maior_total = totais[maior_id]

    if maior_total == 0:
        print("Ainda nao existem entregas finalizadas.")
    else:
        exibir_entregador(maior_id, entregador[maior_id])
        print(f"Entregas finalizadas: {maior_total}")
    input("\n[Pressione Enter para continuar]")

#MENUS

def menu_pedidos():
    executando = True
    while executando:
        limpar_tela()
        print("\n╔═══════════════════════════════╗")
        print("║            PEDIDOS            ║")
        print("║ 1 - Cadastrar Pedido          ║")
        print("║ 2 - Alterar Status            ║")
        print("║ 3 - Cancelar Pedido           ║")
        print("║ 4 - Associar Entregador       ║")
        print("║ 5 - Remover Associacao        ║")
        print("║ 6 - Pedidos Pendentes         ║")
        print("║ 7 - Pedidos Em Rota           ║")
        print("║ 8 - Pedidos Entregues         ║")
        print("║ 9 - Buscar por ID             ║")
        print("║ 0 - Voltar                    ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastro_pedido()
            case "2":
                alterar_status_pedido()
            case "3":
                cancelar_pedido()
            case "4":
                associar_entregador()
            case "5":
                remover_associacao()
            case "6":
                pedidos_pendentes()
            case "7":
                pedidos_em_rota()
            case "8":
                pedidos_entregues()
            case "9":
                buscar_pedido_por_id()
            case "0":
                executando = False
            case _:
                print("Opção inválida.")
                input("\n[Pressione Enter para continuar]")


def menu_entregadores():
    executando = True
    while executando:
        limpar_tela()
        print("\n╔═══════════════════════════════╗")
        print("║         ENTREGADORES          ║")
        print("║ 1 - Cadastrar Entregador      ║")
        print("║ 2 - Disponiveis               ║")
        print("║ 3 - Buscar por ID             ║")
        print("║ 4 - Entregas Realizadas       ║")
        print("║ 0 - Voltar                    ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastro_entregador()
            case "2":
                entregadores_disponiveis()
            case "3":
                buscar_entregador_por_id()
            case "4":
                entregas_realizadas_por_entregador()
            case "0":
                executando = False
            case _:
                print("Opção inválida.")
                input("\n[Pressione Enter para continuar]")


def menu_relatorios():
    executando = True
    while executando:
        limpar_tela()
        print("\n╔═══════════════════════════════╗")
        print("║          RELATÓRIOS           ║")
        print("║ 1 - Total de Pedidos          ║")
        print("║ 2 - Pedidos por Status        ║")
        print("║ 3 - Alta Prioridade           ║")
        print("║ 4 - Maior Numero de Entregas  ║")
        print("║ 0 - Voltar                    ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                relatorio_total_pedidos()
            case "2":
                relatorio_pedidos_por_status()
            case "3":
                relatorio_alta_prioridade()
            case "4":
                relatorio_entregador_maior_entregas()
            case "0":
                executando = False
            case _:
                print("Opção inválida.")
                input("\n[Pressione Enter para continuar]")


def menu_principal():
    executando = True
    while executando:
        limpar_tela()
        print("\n╔═══════════════════════════════╗")
        print("║       FLUXONORTE SYSTEM       ║")
        print("║                               ║")
        print("║ 1 - Pedidos                   ║")
        print("║ 2 - Entregadores              ║")
        print("║ 3 - Relatorios                ║")
        print("║ 0 - Finalizar Sistema         ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                menu_pedidos()
            case "2":
                menu_entregadores()
            case "3":
                menu_relatorios()
            case "0":
                print("Finalizando o sistema...")
                executando = False
            case _:
                print("Opção inválida.")
                input("\n[Pressione Enter para continuar]")


menu_principal()