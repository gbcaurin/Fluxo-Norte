# Enrico
from cadastro import *

STATUS_VALIDOS = ("Pendente", "Em Rota", "Entregue", "Cancelado")


def normalizar_status(status):
    for status_valido in STATUS_VALIDOS:
        if status.lower() == status_valido.lower():
            return status_valido
    return status


def exibir_pedido(id_pedido, info):
    id_entregador = info.get("entregador") or "Nao associado"
    print("-" * 50)
    print(f"ID: {id_pedido}")
    print(f"Cliente: {info.get('nome_cliente', 'Nao informado')}")
    print(f"Endereco: {info.get('endereco', 'Nao informado')}")
    print(f"Prioridade: {info.get('prioridade', 'Nao informado').title()}")
    print(f"Descricao: {info.get('descricao', 'Nao informado')}")
    print(f"Status: {normalizar_status(info.get('status', 'Nao informado'))}")
    print(f"Entregador: {id_entregador}")


def exibir_entregador(id_entregador, info):
    disponibilidade = info.get("status")
    if disponibilidade == True:
        disponibilidade = "Disponivel"
    else:
        disponibilidade = "Indisponivel"

    print("-" * 50)
    print(f"ID: {id_entregador}")
    print(f"Nome: {info.get('nome', 'Nao informado')}")
    print(f"Veiculo: {info.get('veiculo', 'Nao informado')}")
    print(f"Disponibilidade: {disponibilidade}")


def listar_pedidos_status(status_desejado):
    encontrados = False
    status_desejado = status_desejado.lower()

    for id_pedido, info in pedidos.items():
        status_atual = str(info.get("status", "")).lower()
        if status_atual == status_desejado:
            exibir_pedido(id_pedido, info)
            encontrados = True

    if not encontrados:
        print("\nNenhum pedido encontrado para este status.")
    
    input("\n[Pressione Enter para continuar]")


def pedidos_pendentes():
    print("\nPedidos Pendentes")
    listar_pedidos_status("Pendente")


def pedidos_entregues():
    print("\nPedidos Entregues")
    listar_pedidos_status("Entregue")


def buscar_pedido_por_id():
    id_pedido = input("Digite o ID do pedido (ex: P0001): ").upper()

    if not validar_id_pedido(id_pedido):
        print("\nID de pedido invalido.")
        input("\n[Pressione Enter para continuar]")
        return

    if id_pedido not in pedidos:
        print("\nPedido nao encontrado.")
    else:
        exibir_pedido(id_pedido, pedidos[id_pedido])

    input("\n[Pressione Enter para continuar]")


def entregadores_disponiveis():
    print("\nEntregadores Disponiveis")
    encontrados = False

    for id_entregador, info in entregador.items():
        if info.get("status") is True or str(info.get("status", "")).lower() == "disponivel":
            exibir_entregador(id_entregador, info)
            encontrados = True

    if not encontrados:
        print("\nNenhum entregador disponivel no momento.")

    input("\n[Pressione Enter para continuar]")


def buscar_entregador_por_id():
    id_entregador = input("Digite o ID do entregador: ")

    if not validar_id_entregador(id_entregador):
        print("\nID de entregador invalido.")
        input("\n[Pressione Enter para continuar]")
        return

    if id_entregador not in entregador:
        print("\nEntregador nao encontrado.")
    else:
        exibir_entregador(id_entregador, entregador[id_entregador])

    input("\n[Pressione Enter para continuar]")


def entregas_realizadas_por_entregador():
    id_entregador = input("Digite o ID do entregador: ")

    if not validar_id_entregador(id_entregador):
        print("\nID de entregador invalido.")
        input("\n[Pressione Enter para continuar]")
        return

    if id_entregador not in entregador:
        print("\nEntregador nao encontrado.")
        input("\n[Pressione Enter para continuar]")
        return

    print(f"\nEntregas realizadas por {entregador[id_entregador].get('nome', id_entregador)}")
    encontrados = False

    for id_pedido, info in pedidos.items():
        status_entregue = str(info.get("status", "")).lower() == "entregue"
        mesmo_entregador = info.get("entregador") == id_entregador
        if status_entregue and mesmo_entregador:
            exibir_pedido(id_pedido, info)
            encontrados = True

    if not encontrados:
        print("\nNenhuma entrega realizada por este entregador.")

    input("\n[Pressione Enter para continuar]")


def relatorio_total_pedidos():
    print("\nRelatorio - Total de Pedidos")
    print(f"Total de pedidos cadastrados: {len(pedidos)}")
    input("\n[Pressione Enter para continuar]")


def relatorio_pedidos_por_status():
    print("\nRelatorio - Quantidade de Pedidos por Status")

    for status in STATUS_VALIDOS:
        quantidade = 0
        for info in pedidos.values():
            if str(info.get("status", "")).lower() == status.lower():
                quantidade += 1
        print(f"{status}: {quantidade}")

    input("\n[Pressione Enter para continuar]")


def relatorio_alta_prioridade():
    print("\nRelatorio - Pedidos com Alta Prioridade")
    encontrados = False

    for id_pedido, info in pedidos.items():
        if str(info.get("prioridade", "")).lower() == "alta":
            exibir_pedido(id_pedido, info)
            encontrados = True

    if not encontrados:
        print("\nNenhum pedido de alta prioridade encontrado.")

    input("\n[Pressione Enter para continuar]")


def relatorio_entregador_maior_numero_entregas():
    print("\nRelatorio - Entregador com Maior Numero de Entregas")

    if not entregador:
        print("\nNenhum entregador cadastrado.")
        input("\n[Pressione Enter para continuar]")
        return

    totais = {}
    for id_entregador in entregador:
        totais[id_entregador] = 0

    for info in pedidos.values():
        id_entregador = info.get("entregador")
        status_entregue = str(info.get("status", "")).lower() == "entregue"
        if status_entregue and id_entregador in totais:
            totais[id_entregador] += 1

    maior_id = max(totais, key=totais.get)
    maior_total = totais[maior_id]

    if maior_total == 0:
        print("\nAinda nao existem entregas finalizadas.")
    else:
        exibir_entregador(maior_id, entregador[maior_id])
        print(f"Entregas finalizadas: {maior_total}")

    input("\n[Pressione Enter para continuar]")
