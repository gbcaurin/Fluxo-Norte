# FluxoNorte System

Sistema operacional de logística desenvolvido em Python para a empresa FluxoNorte, como projeto avaliativo da disciplina de Algoritmos de Programação, Projetos e Computação (APPC) — Engenharia de Software, PUC-Campinas.

## Como executar

Requer Python 3.10 ou superior (por conta do `match/case`).

```
python main.py
```

Compatible com IDLE do Python.org e VSCode.

## Funcionalidades

**Pedidos**

- Cadastrar pedido
- Alterar status (Pendente → Em Rota → Entregue)
- Cancelar pedido
- Associar entregador a um pedido
- Remover associação de entregador
- Listar pedidos por status (Pendentes, Em Rota, Entregues)
- Buscar pedido por ID

**Entregadores**

- Cadastrar entregador
- Listar entregadores disponíveis
- Buscar entregador por ID
- Ver todas as entregas realizadas por um entregador

**Relatórios**

- Total de pedidos cadastrados
- Quantidade de pedidos por status
- Pedidos com prioridade Alta
- Entregador com maior número de entregas finalizadas

## Regras de negócio

- Pedidos seguem ordem de chegada (FIFO): o primeiro pedido associado a um entregador é o primeiro a ser entregue
- Cada entregador pode ter no máximo 5 pedidos simultâneos
- Pedido cancelado não pode ser reativado
- Um pedido só pode ir para "Em Rota" se tiver entregador associado
- Um pedido só pode ser marcado como "Entregue" se estiver "Em Rota" e for o mais antigo da fila do entregador

## Estrutura dos dados

Os dados ficam em memória durante a execução. Não há banco de dados ou arquivos externos.

**Pedido:**

```
{
  "nome_cliente": str,
  "endereco": str,
  "prioridade": "alta" ou "normal",
  "descricao": str,
  "status": "Pendente" | "Em Rota" | "Entregue" | "Cancelado",
  "entregador": str (ID) ou None
}
```

**Entregador:**

```
{
  "nome": str,
  "veiculo": "carro" | "van" | "moto" | "bicicleta" | "patinete",
  "pedidos": [lista de IDs de pedidos],
  "status": True (disponível) | False (indisponível)
}
```

## Time

Projeto desenvolvido em grupo para a disciplina APPC — PUC-Campinas, 2026.
