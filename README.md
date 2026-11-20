# Cadastro de Produtos

Atividade N3 – Estrutura de Dados e Organização de Arquivos

**Aluno:** Lucas Gabriel Amorim Steffen

## Sobre o projeto
Sistema de cadastro de produtos feito em Python, que roda no terminal. Os dados
ficam salvos em um arquivo JSON (`products.json`), então não se perdem quando o
programa é fechado.

## Como executar
É preciso ter o Python 3 instalado. Não precisa instalar nada além disso.

```bash
python registrations.py
```

## O que o programa faz
| Requisito da atividade | Como foi feito |
|------------------------|----------------|
| Incluir, alterar e excluir | Opções 1, 2 e 3 do menu |
| Salvar em JSON | O programa lê e grava tudo no `products.json` |
| Pesquisa por campo de texto | Buscar por nome e por categoria |
| Lista ordenada por 2 campos | Ordenar por nome (A-Z) e por preço (menor para maior) |

## Menu
```
=== MENU ===
0 - Ver todos
1 - Incluir
2 - Atualizar
3 - Excluir
9 - Sair
```

- **0 - Ver todos:** mostra a tabela de produtos e abre outro menu, com as
  buscas e as ordenações:
  ```
  1 - Buscar por id
  2 - Buscar por nome
  3 - Buscar por categoria
  4 - Ordenar por nome (A-Z)
  5 - Ordenar por preço (menor para maior)
  0 - Voltar
  ```
- **1 - Incluir:** pede nome, categoria, preço e quantidade. O id é criado
  automaticamente.
- **2 - Atualizar:** pede o id e pergunta qual campo mudar (nome, categoria,
  preço, quantidade ou todos), para não precisar digitar tudo de novo.
- **3 - Excluir:** pede o id e uma confirmação (s/n) antes de apagar.

As buscas aceitam só um pedaço do texto e não diferenciam maiúscula de minúscula.

## Exemplo
```
ID   Nome                     Categoria              Preço   Qtd
----------------------------------------------------------------
3    Clear Men                Shampoo                39.90     1
4    Ração Pedigree           Rações                999.00     1
5    PC Xuxa                  Computadores           15.00    50
```

## Como os dados são salvos
O `products.json` é uma lista, e cada produto tem estes campos:

```json
{
    "id": 3,
    "name": "Clear Men",
    "category": "Shampoo",
    "price": 39.9,
    "quantity": 1
}
```

## Funções principais
| Função | O que faz |
|--------|-----------|
| `load_data` / `save_data` | Lê e grava o arquivo JSON |
| `read_text`, `read_intNumber`, `read_float` | Pedem os dados ao usuário e não aceitam valor vazio, inválido ou negativo |
| `findById` | Procura um produto pelo id |
| `include`, `change`, `delete` | Incluir, atualizar e excluir produto |
| `search_by_id`, `search_by_name`, `search_by_category` | Buscas |
| `sort_by_name`, `sort_by_price` | Ordenações (usam `sorted()`) |
| `show_products` | Mostra a tabela na tela |
| `menu`, `view_menu` | Menu principal e menu do "Ver todos" |
