#Gabriel
import os

pedidos = {}
entregador = {}
contador_pedidos = 1
contador_entregadores = 1001

def limpar():
  os.system('cls')

def entregadores():
  print("Entregadores cadastrados:")
  for id, info in entregador.items():
    print(f"ID: {id}, Nome: {info['nome']}, Veículo: {info['veiculo']}, Status: {info['status']}")

  input("[Pressione Enter para retornar]")
  limpar()

def pedidos_cadastrados():
  print("Pedidos cadastrados:")
  for id, info in pedidos.items():
    print(f"ID: {id}, Cliente: {info['nome_cliente']}, Endereço: {info['endereco']}, Prioridade: {info['prioridade']}, Status: {info['status']}")

  input("[Pressione Enter para retornar]")
  limpar()

def validar_id_pedido(id): 
    if len(id) == 5 and id[0] == 'P' and id[1:].isdigit():
        return True
    return False

def validar_id_entregador(id):
    if len(id) == 4 and id.isdigit():
        return True
    else:
        return False

def gerar_id_entregador():
  global contador_entregadores
  id = str(contador_entregadores)
  contador_entregadores += 1
  return id

def gerar_id_pedido():
  global contador_pedidos
  id = f"P{contador_pedidos:04d}"
  contador_pedidos += 1
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

  if validar_id_pedido(id) and id not in pedidos:
    pedidos[id] = {"nome_cliente": nome_cliente, "endereco": endereco, "prioridade": prioridade, "descricao": descricao, "status": "Pendente", "entregador": None}
    print(f"Pedido cadastrado com ID: {id}")

  limpar()

  def cadastro_entregador():
    id = gerar_id_entregador()
    nome = input("Digite o nome do entregador: ")
    veiculo = input("Digite o tipo de veículo do entregador: ")

    for info in entregador.values():
      if info["nome"].lower() == nome.lower():
        print("Entregador já cadastrado.")
        limpar()
        return

    if validar_id_entregador(id) and id not in entregador:
      entregador[id] = {"nome": nome, "veiculo": veiculo, "pedidos": [], "status": True}
      print(f"Entregador cadastrado com ID: {id}")
    else:
      print("Falha no cadastro do entregador. ID inválido ou já existente.")

    limpar()

def main():
  limpar()
  while True:
    print("1. Cadastrar Pedido")
    print("2. Cadastrar Entregador")
    print("3. Ver Entregadores Cadastrados")
    print("4. Ver Pedidos Cadastrados")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    match escolha:
      case "1":
        limpar()
        cadastro_pedido()
      case "2":
        limpar()
        cadastro_entregador()
      case "5":
        print("Saindo do programa.")
        break
      case "3":
        limpar()
        entregadores()
      case "4":
        limpar()
        pedidos_cadastrados()
      case _:
        limpar()
        print("Opção inválida. Tente novamente.")
        print("-" * 30)

main()