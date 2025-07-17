# Hortifruti Sensação - Simulador de Caixa em Python

Este é um simulador de caixa para um hortifrúti, desenvolvido em Python, com interface de console. O projeto demonstra aplicações práticas de diversas estruturas de dados como dicionários, filas, tuplas, pilhas e conjuntos. O sistema simula o fluxo de um cliente montando seu carrinho, sendo atendido por um caixa e efetuando o pagamento.

---

##  Funcionalidades Principais
- **Catálogo de Produtos:** Gerencia produtos com código, nome, preço e estoque.
- **Fila de Clientes:** Simula a fila de clientes aguardando atendimento no caixa.
- **Carrinho de Compras:** Clientes podem "montar" seus carrinhos com produtos e quantidades.
- **Processamento de Compra:** O caixa escaneia os itens, verifica o estoque e aplica promoções.
- **Pagamento e Troco:** Simula a etapa de pagamento, calculando o troco.
- **Promoções:** Produtos podem ser marcados com preço promocional.

---

## 1. Descrição do Problema Resolvido
Este projeto aborda o problema de simular as operações essenciais de um caixa em um ambiente de varejo, como um hortifrúti. O objetivo é recriar o fluxo de atendimento ao cliente, desde a seleção dos produtos até o pagamento, considerando aspectos como controle de estoque, aplicação de promoções e gerenciamento da fila de clientes. O simulador permite visualizar e interagir com essas etapas de forma simplificada, demonstrando como diferentes estruturas de dados podem ser utilizadas para modelar cenários do mundo real.

---

## 2. Justificativa da Escolha do Tema
- **Familiaridade e Relevância:** É um cenário do cotidiano, fácil de entender e relacionar, o que facilita a visualização do problema e das soluções.
- **Complexidade Adequada para Aprendizado:** Permite a aplicação de várias estruturas de dados fundamentais sem se tornar excessivamente complexo.
- **Potencial de Expansão:** Pode crescer com mais funcionalidades como diferentes métodos de pagamento, relatórios de vendas, sistema de desfazer, etc.
- **Aplicação Prática das Estruturas de Dados:** Demonstra como a escolha correta da estrutura pode otimizar desempenho e clareza.

---

## 3.  Descrição e Justificativa das Estruturas de Dados Aplicadas

### a) Dicionários
- **Aplicação:** Armazenar o catálogo de produtos (`self.produtos`), com código como chave e valores como outro dicionário: `{ 'produto': 'Nome', 'preco': valor, 'estoque': quantidade }`
- **Justificativa:**
  - Acesso rápido por chave (O(1))
  - Agrupamento organizado de atributos do produto
  - Flexível para atualização e remoção

### b) Filas
- **Aplicação:** Gerenciar a fila de clientes (`self.fila_clientes`)
- **Justificativa:**
  - Comportamento FIFO realista (deque do módulo `collections`)
  - Operações eficientes para grandes volumes

### c) Tuplas
- **Aplicação:** Representar itens no carrinho: lista de tuplas como `[('001', 3), ('004', 2)]`
- **Justificativa:**
  - Imutabilidade garante integridade dos dados
  - Leves e eficientes

### d) Conjuntos
- **Aplicação:** Armazenar códigos de produtos em promoção (`self.produtos_em_promocao`)
- **Justificativa:**
  - Garante unicidade
  - Verificação rápida (O(1)) para saber se há promoção

### e) Pilha
- **Aplicação:** Armazenar histórico das vendas (`self.historico_caixa`)
- **Justificativa:**
  - Comportamento LIFO útil para auditoria e desfazer
  - Fácil de implementar com listas (`append` e `pop`)

---

## 4. Desafios Enfrentados e Soluções Encontradas

### Desafio 1: Gerenciamento do Estado da Compra Atual
- **Problema:** Toda a lógica de cálculo e pagamento estava acoplada em `atender_proximo_cliente`
- **Solução:** Separação em dois métodos: `atender_proximo_cliente` (escanear) e `processar_pagamento` (pagar). Uso de atributos `self.total_compra_atual` e `self.carrinho_em_processo`

### Desafio 2: Validação de Entrada do Usuário
- **Problema:** Erros causados por entradas inesperadas (ex: letras, negativos, vírgulas)
- **Solução:** `try-except`, `.strip()`, `.replace(',', '.')`, e verificações de valores válidos

### Desafio 3: Clareza na Visualização da Fila e Produtos
- **Problema:** Saídas pouco informativas
- **Solução:** Melhor formatação `print()`, com alinhamento e indicação de promoções

---

## 5. Como Usar o Simulador

### Pré-requisitos
- Python 3 instalado

### Iniciando o Simulador
1. Salve como `hortifruti_simulador.py`
2. Execute:
```bash
python hortifruti_simulador.py
```
3. Ou pressione `F5` no VSCode

---

## 6. Menu Principal
```
===== Menu do Simulador Hortifrúti ======
1. Listar Produtos
2. Cliente Chega (Montar Carrinho)
3. Atender Próximo Cliente (Escanear)
4. Processar Pagamento
5. Ver Fila de Clientes
6. Adicionar Produto (Admin)
7. Remover Produto (Admin)
8. Adicionar Promoção (Admin)
9. Remover Promoção (Admin)
0. Sair
========================================
```

---

## 7. Opções do Menu Detalhadas

### 1. Listar Produtos
Mostra código, nome, preço e estoque. Indica se o produto está em promoção.

### 2. Cliente Chega (Montar Carrinho)
Cliente monta um carrinho:
- Informe o código do produto e a quantidade
- Digite `fim` para concluir
- Carrinho vai para a fila

### 3. Atender Próximo Cliente (Escanear)
- Caixa escaneia produtos do primeiro cliente na fila
- Aplica promoções e calcula total (mas **não** finaliza a compra)

### 4. Processar Pagamento
- Solicita valor pago
- Calcula e exibe troco
- Finaliza compra e salva no histórico

### 5. Ver Fila de Clientes
- Exibe número de clientes na fila e prévia do carrinho do próximo

### 6 a 9. Funções Admin
- **6. Adicionar Produto:** Adiciona novo item ao catálogo
- **7. Remover Produto:** Remove item do catálogo
- **8. Adicionar Promoção:** Marca um produto com desconto
- **9. Remover Promoção:** Remove item da lista de promoções

### 0. Sair
Encerra o simulador

---

## 8. Exemplo de Fluxo de Uso
1. Escolha `1` para ver produtos
2. Escolha `2` para montar o carrinho
3. Escolha `5` para ver a fila
4. Escolha `3` para escanear itens
5. Escolha `4` para simular pagamento

---

## Licença
Este projeto é de livre uso para fins educacionais.

---

## Contribuição
Sugestões, melhorias ou correções são bem-vindas. Abra um Pull Request ou envie uma sugestão via issues!

---

**Desenvolvido em Python para fins didáticos.**

