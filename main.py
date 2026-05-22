import os

#Importação dos módulos
from cadastro import *
from atualizacoes import *
from consulta import *

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



# ======================================
# MENU PEDIDOS
# ======================================


def menu_pedidos():
    executando = True

    while executando:
        limpar_tela()

        print("\n╔═══════════════════════════════╗")
        print("║            PEDIDOS           ║")
        print("║ 1 - Cadastrar Pedido         ║")
        print("║ 2 - Atualizar Pedido         ║")
        print("║ 3 - Pedidos Pendentes        ║")
        print("║ 4 - Pedidos Entregues        ║")
        print("║ 5 - Buscar Pedido por ID     ║")
        print("║ 0 - Voltar                   ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")
        match opcao:

            case "1":
                print("\n Cadastro do pedido...")
                print("Pressione ENTER para continuar...")
            
            case "2":
                print("\n Atualização do Pedido...")
                print("Pressione ENTER para continuar...")

            case "3":
                print("\n Pedidos Pendentes...")
                print("Pressione ENTER para continuar...")

            case "4":
                print("\n Pedidos Entregues...")
                print("Pressione ENTER para continuar...")
            
            case "5":
                print("\n Buscar Pedido por ID...")
                print("Pressione ENTER para continuar...")

            case "0":
                print("\n Voltando ao menu principal...")
                executando = False

            case _:
                print("\n Esta opção é inválida.")
                print("Pressione ENTER para continuar...")


# ======================================
# MENU PEDIDOS
# ======================================


def menu_entregadores():
    executando = True

    while executando:
        limpar_tela()

        print("\n╔═══════════════════════════════╗")
        print("║         ENTREGADORES         ║")
        print("║ 1 - Cadastrar Entregador     ║")
        print("║ 2 - Atualizar Entregador     ║")
        print("║ 3 - Disponíveis              ║")
        print("║ 4 - Buscar por ID            ║")
        print("║ 5 - Entregas Realizadas      ║")
        print("║ 0 - Voltar                   ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")    
        match opcao:

            case "1":
                print("\n Cadastro do Entregador...")
                print("Pressione ENTER para continuar...")
            
            case "2":
                print("\n Atualização do Entregador...")
                print("Pressione ENTER para continuar...")  

            case "3":
                print("\n Entregadores Disponíveis...")
                print("Pressione ENTER para continuar...")

            case "4":
                print("\n Buscar Entregador por ID...")
                print("Pressione ENTER para continuar...")

            case "5":
                print("\n Entregas Realizadas...")
                print("Pressione ENTER para continuar...")

            case "0":
                print("\n Voltando ao menu principal...")
                executando = False

            case _:
                print("\n Esta opção é inválida.")
                print("Pressione ENTER para continuar...")


# ======================================
# MENU RELATORIOS
# ======================================

def menu_relatorios():
    executando = True

    while executando:
        limpar_tela()

        print("\n╔═══════════════════════════════╗")
        print("║          RELATÓRIOS          ║")
        print("║ 1 - Total de Pedidos         ║")
        print("║ 2 - Pedidos por Status       ║")
        print("║ 3 - Alta Prioridade          ║")
        print("║ 4 - Maior Número Entregas    ║")
        print("║ 0 - Voltar                   ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":
            print("\n Total de Pedidos Realizados...")
            print("Pressione ENTER para continuar...")

        case "2":
            print("\n Lista de Pedidos por Status...")
            print("Pressione ENTER para continuar...")

        case "3":
            print("\n Pedidos de Alta Prioridade...")
            print("Pressione ENTER para continuar...")
        
        case "4":
            print("\n Maior Número de Entregas...")
            print("Pressione ENTER para continuar...")

        case "0":
            print("\n Voltando ao Menu Principal...")
            executando = False

        case _:
            print("\n Esta opção é inválida.")
            print("Pressione ENTER para continuar...")      


# ======================================
# MENU PRINCIPAL
# ======================================

def menu_principal():
    executando = True

    while executando:
        limpar_tela()

        print("\n╔═══════════════════════════════╗")
        print("║       FLUXONORTE SYSTEM      ║")
        print("║                               ║")
        print("║ 1 - Pedidos                  ║")
        print("║ 2 - Entregadores             ║")
        print("║ 3 - Relatórios               ║")
        print("║ 4 - Consultas                ║")
        print("║ 0 - Finalizar Sistema        ║")
        print("╚═══════════════════════════════╝")

        opcao = input("Escolha uma opção: ")    
        match opcao:

            case "1":
                menu_pedidos()

            case "2":
                menu_entregadores()

            case "3":
                menu_relatorios()

            case "4":
                print("\n Consultas...")
                print("Pressione ENTER para continuar...")

            case "0":
                print("\n Finalizando o sistema...")
                executando = False

            case _:
                print("\n Esta opção é inválida.")
                print("Pressione ENTER para continuar...")

# ======================================
# INICIAR SISTEMA
# ======================================

menu_principal()