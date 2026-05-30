limite_pedidos = 5


# Busca um pedido pelo ID
def buscar_pedido(pedidos, id_pedido):
    for p in pedidos:
        if p["id"] == id_pedido:
            return p
    return None


# Busca um entregador pelo ID
def buscar_entregador(entregadores, id_entregador):
    for e in entregadores:
        if e["id"] == id_entregador:
            return e
    return None


# Altera o status do pedido
def alterar_status_pedido(pedidos, entregadores):
    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(pedidos, id_pedido)

    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Cancelado":
        print("Pedido cancelado nao pode ser alterado.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao pode ser alterado.")
        return

    print(" 1-Pendente | 2-Em Rota | 3-Entregue ")
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

    # Nao pode ir pra "Em Rota" sem entregador
    if novo == "Em Rota" and pedido["id_entregador"] == "":
        print("Pedido sem entregador nao pode ir pra Em Rota.")
        return

    # So entrega quem esta Em Rota
    if novo == "Entregue" and pedido["status"] != "Em Rota":
        print("So entrega pedido que esta Em Rota.")
        return

    # Entrega respeita ordem de chegada (FIFO)
    if novo == "Entregue":
        entrega = buscar_entregador(entregadores, pedido["id_entregador"])
        if entrega is not None and len(entrega["pedidos"]) > 0:
            if entrega["pedidos"][0] != pedido["id"]:
                print("Tem pedido mais antigo na fila, entregue ele primeiro.")
                return
            entrega["pedidos"].remove(pedido["id"])
            entrega["disponibilidade"] = True

    pedido["status"] = novo
    print("Status atualizado para:", novo)


# Cancela um pedido (definitivo)
def cancelar_pedido(pedidos, entregadores):
    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(pedidos, id_pedido)

    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Cancelado":
        print("Pedido ja esta cancelado.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao pode ser cancelado.")
        return

    # Desvincula o entregador, se tiver
    if pedido["id_entregador"] != "":
        entrega = buscar_entregador(entregadores, pedido["id_entregador"])
        if entrega is not None:
            if id_pedido in entrega["pedidos"]:
                entrega["pedidos"].remove(id_pedido)
            entrega["disponibilidade"] = True

    pedido["id_entregador"] = ""
    pedido["status"] = "Cancelado"
    print("Pedido cancelado.")


# Associa um entregador a um pedido
def associar_entregador(pedidos, entregadores):
    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(pedidos, id_pedido)

    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Cancelado":
        print("Pedido cancelado nao recebe entregador.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao recebe entregador.")
        return

    if pedido["id_entregador"] != "":
        print("Pedido ja tem entregador.")
        return

    id_entregador = input("ID do entregador: ").strip()
    entrega = buscar_entregador(entregadores, id_entregador)

    if entrega is None:
        print("Entregador nao encontrado.")
        return

    if not entrega["disponibilidade"]:
        print("Entregador indisponivel.")
        return

    if len(entrega["pedidos"]) >= limite_pedidos:
        print("Entregador atingiu o limite de", limite_pedidos, "pedidos.")
        return

    # Evita pedido repetido na lista
    if id_pedido in entrega["pedidos"]:
        print("Pedido ja esta na lista do entregador.")
        return

    # Faz a associacao (append mantem ordem de chegada)
    pedido["id_entregador"] = id_entregador
    pedido["status"] = "Em Rota"
    entrega["pedidos"].append(id_pedido)

    # Se encheu, marca indisponivel
    if len(entrega["pedidos"]) >= limite_pedidos:
        entrega["disponibilidade"] = False

    print("Entregador associado e pedido Em Rota.")


# Remove a associacao entre entregador e pedido
def remover_associacao(pedidos, entregadores):
    id_pedido = input("ID do pedido: ").upper()
    pedido = buscar_pedido(pedidos, id_pedido)

    if pedido is None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Entregue":
        print("Pedido entregue nao pode desvincular.")
        return

    if pedido["id_entregador"] == "":
        print("Pedido nao tem entregador.")
        return

    # Tira o pedido da lista do entregador
    entrega = buscar_entregador(entregadores, pedido["id_entregador"])
    if entrega is not None:
        if id_pedido in entrega["pedidos"]:
            entrega["pedidos"].remove(id_pedido)
        entrega["disponibilidade"] = True

    pedido["id_entregador"] = ""
    pedido["status"] = "Pendente"
    print("Associação removida, pedido voltou pra Pendente.")


# Mostra o proximo pedido da fila do entregador (FIFO)
def proximo_pedido_entregador(pedidos, entregadores):
    id_entregador = input("ID do entregador: ")
    entrega = buscar_entregador(entregadores, id_entregador)

    if entrega is None:
        print("Entregador nao encontrado.")
        return

    if len(entrega["pedidos"]) == 0:
        print("Entregador sem pedidos na fila.")
        return

    # Primeiro da lista = mais antigo
    pedido = buscar_pedido(pedidos, entrega["pedidos"][0])
    print("Proximo de", entrega["nome"] + ":")
    print("   ID:", pedido["id"])
    print("   Cliente:", pedido["cliente"])
    print("   Status:", pedido["status"])