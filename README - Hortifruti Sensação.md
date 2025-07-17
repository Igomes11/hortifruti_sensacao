## README: Hortifruti Sensação (Python)

Este documento descreve como usar o simulador de caixa de hortifruti,
uma aplicação em console desenvolvida em Python que demonstra o uso de
**dicionários**, **filas**, **tuplas, pilhas** e **conjuntos**. O
sistema simula o fluxo de um cliente montando seu carrinho, sendo
atendido por um caixa e efetuando o pagamento.

### Funcionalidades Principais

- **Catálogo de Produtos:** Gerencia produtos com código, nome, preço e
  > estoque.

- **Fila de Clientes:** Simula a fila de clientes aguardando atendimento
  > no caixa.

- **Carrinho de Compras:** Clientes podem \"montar\" seus carrinhos com
  > produtos e quantidades.

- **Processamento de Compra:** O caixa escaneia os itens, verifica o
  > estoque e aplica promoções.

- **Pagamento e Troco:** Simula a etapa de pagamento, calculando o
  > troco.

- **Promoções:** Produtos podem ser marcados com preço promocional.

- **Histórico de Vendas:** As vendas finalizadas são registradas em um
  > histórico (pilha).

### 1. Descrição do Problema Resolvido {#descrição-do-problema-resolvido}

Este projeto aborda o problema de **simular as operações essenciais de
um caixa em um ambiente de varejo, como um hortifrúti**. O objetivo é
recriar o fluxo de atendimento ao cliente, desde a seleção dos produtos
até o pagamento, considerando aspectos como controle de estoque,
aplicação de promoções e gerenciamento da fila de clientes. O simulador
permite visualizar e interagir com essas etapas de forma simplificada,
demonstrando como diferentes estruturas de dados podem ser utilizadas
para modelar cenários do mundo real.

### 2. Justificativa da Escolha do Tema {#justificativa-da-escolha-do-tema}

A escolha do tema \"Simulador de Caixa de Hortifrúti\" se deu por
diversos motivos:

- **Familiaridade e Relevância:** É um cenário do cotidiano, fácil de
  > entender e relacionar, o que facilita a visualização do problema e
  > das soluções. Operações de caixa são universais no comércio.

- **Complexidade Adequada para Aprendizado:** Apresenta uma complexidade
  > equilibrada, permitindo a aplicação de várias estruturas de dados
  > fundamentais (dicionários, filas, tuplas e conjuntos) sem se tornar
  > excessivamente complexo.

- **Potencial de Expansão:** O projeto é facilmente expansível para
  > incluir mais funcionalidades, como diferentes métodos de pagamento,
  > relatórios de vendas, gerenciamento de funcionários, sistema de
  > \"desfazer\", etc., o que o torna um bom ponto de partida para
  > futuros desenvolvimentos.

- **Aplicação Prática das Estruturas de Dados:** É um excelente caso de
  > uso para demonstrar como a escolha correta da estrutura de dados
  > pode otimizar o desempenho e a clareza do código em situações
  > práticas.

### 3. Descrição e Justificativa das Estruturas de Dados Aplicadas {#descrição-e-justificativa-das-estruturas-de-dados-aplicadas}

O projeto faz uso extensivo das seguintes estruturas de dados do Python:

#### a) Dicionários  {#a-dicionários}

- **Aplicação:** Utilizado principalmente para armazenar o **catálogo de
  > produtos** (self.produtos). Cada chave é o **código único do
  > produto** (string), e seu valor é outro dicionário contendo detalhes
  > como {\'produto\': \'Nome\', \'preco\': valor, \'estoque\':
  > quantidade}.

- **Justificativa da Escolha:**

  - **Acesso Rápido por Chave:** Dicionários oferecem acesso de tempo
    > constante (O(1) em média) aos valores através de suas chaves. Isso
    > é crucial para consultar rapidamente informações de um produto ao
    > escanear seu código ou verificar seu estoque.

  - **Modelagem de Entidades:** Permite agrupar atributos relacionados
    > (nome, preço, estoque) para cada produto de forma organizada e
    > legível.

  - **Flexibilidade:** Facilita a adição, remoção e atualização de
    > produtos no catálogo.

#### b) Filas  {#b-filas}

- **Aplicação:** Usada para gerenciar a **fila de clientes**
  > (self.fila_clientes) que aguardam atendimento no caixa. Cada
  > \"cliente\" na fila é, na verdade, o seu carrinho_de_compras (uma
  > lista de tuplas).

- **Justificativa da Escolha:**

  - **Comportamento FIFO (First-In, First-Out):** A deque (fila de duas
    > pontas) do módulo collections é otimizada para operações de
    > adicionar (append()) e remover (popleft()) de ambas as
    > extremidades em tempo constante (O(1)). Isso simula perfeitamente
    > o comportamento de uma fila real de supermercado, onde o primeiro
    > cliente a chegar é o primeiro a ser atendido.

  - **Eficiência:** Mais eficiente para operações de fila do que uma
    > lista Python padrão para grandes volumes de dados, onde
    > list.pop(0) pode ser lento (O(n)).

#### c) Tuplas

- **Aplicação:** Utilizadas para representar **itens individuais dentro
  > do carrinho de compras** ((codigo_produto, quantidade)). O carrinho
  > em si é uma **lista de tuplas**. Por exemplo, \[(\'001\', 3),
  > (\'004\', 2)\].

- **Justificativa da Escolha:**

  - **Imutabilidade:** Tuplas são imutáveis. Uma vez que um item é
    > adicionado ao carrinho com um código e uma quantidade, essa
    > \"combinação\" específica (código e quantidade) não deve ser
    > alterada acidentalmente. Isso garante a integridade dos dados do
    > item no momento da seleção.

  - **Leveza e Desempenho:** Tuplas são geralmente mais eficientes em
    > termos de memória e um pouco mais rápidas que listas para
    > armazenar coleções fixas de itens.

#### d) Conjuntos  {#d-conjuntos}

- **Aplicação:** Utilizado para armazenar os **códigos dos produtos que
  > estão em promoção** (self.produtos_em_promocao).

- **Justificativa da Escolha:**

  - **Unicidade:** Conjuntos armazenam apenas elementos únicos,
    > garantindo que um produto não seja listado como em promoção
    > múltiplas vezes.

  - **Testes de Pertença Rápidos:** A principal vantagem é a eficiência
    > na verificação se um elemento está presente no conjunto (operação
    > in). A verificação é de tempo constante (O(1) em média), o que é
    > ideal para checar rapidamente se um produto escaneado tem
    > promoção.

  - **Operações de Conjuntos:** Embora não amplamente exploradas neste
    > projeto, conjuntos também permitem operações como união,
    > interseção e diferença, que poderiam ser úteis em cenários mais
    > complexos de gerenciamento de promoções.

#### e) Pilha

- **Aplicação:** A lista padrão do Python é utilizada como uma **pilha**
  > para o self.historico_caixa. Cada elemento adicionado é um
  > dicionário que representa uma transação de venda completa, com
  > detalhes como total, itens vendidos, valor pago e troco.

- **Justificativa da Escolha:**

  - **Comportamento LIFO (Last-In, First-Out):** Listas Python podem
    > simular uma pilha eficientemente usando append() para adicionar ao
    > \"topo\" e pop() para remover do \"topo\" (final da lista). Isso é
    > ideal para um histórico de ações, onde você geralmente quer
    > reverter ou consultar a ação mais recente.

  - **Simplicidade:** Para uma pilha de operações simples, a lista
    > Python é uma escolha prática e performática o suficiente.

### 4. Desafios Enfrentados e Soluções Encontradas {#desafios-enfrentados-e-soluções-encontradas}

Durante o desenvolvimento do simulador, alguns desafios foram
identificados e soluções implementadas:

- **Desafio 1: Gerenciamento do Estado da Compra Atual.**

  - **Problema:** Inicialmente, a lógica de cálculo do total e de
    > pagamento estava toda dentro de atender_proximo_cliente. Isso
    > dificultava a separação das etapas de \"escanear\" e \"pagar\" e
    > tornava o fluxo menos modular. Se o usuário quisesse apenas ver o
    > total antes de pagar, seria complicado.

  - **Solução:** Introdução de atributos de classe
    > self.total_compra_atual e self.carrinho_em_processo. A função
    > atender_proximo_cliente agora foca apenas em processar os itens do
    > carrinho da fila, calcular o total e atualizar o estoque,
    > armazenando esses dados nos novos atributos. Uma função
    > processar_pagamento separada foi criada para lidar exclusivamente
    > com a interação de pagamento, acessando esses atributos. Isso
    > permitiu a adição de uma opção \"Pagar\" no menu principal,
    > oferecendo maior controle e modularidade.

- **Desafio 2: Validação de Entrada do Usuário.**

  - **Problema:** Entradas de usuário via input() são strings e podem
    > conter caracteres inválidos ou formatos inesperados (ex: texto
    > onde se espera um número, números negativos para quantidade, ou
    > decimais com vírgula). Isso poderia causar erros no programa.

  - **Solução:** Implementação de blocos try-except ValueError para
    > converter entradas de string para números (int ou float). Adição
    > de .strip() para remover espaços em branco e .replace(\',\',
    > \'.\') para aceitar vírgulas como separador decimal. Além disso,
    > foram adicionadas verificações explícitas para quantidades
    > positivas e códigos de produto existentes, fornecendo feedback
    > claro ao usuário.

- **Desafio 3: Clareza na Visualização da Fila e Produtos.**

  - **Problema:** As listagens iniciais da fila ou produtos poderiam ser
    > pouco informativas ou difíceis de ler para o usuário.

  - **Solução:** Formatação aprimorada das saídas print(). Na listagem
    > de produtos, adicionei a indicação (PROMOÇÃO!) quando aplicável e
    > alinhei as colunas. Para a visualização da fila, adicionei uma
    > prévia dos itens do carrinho do próximo cliente, tornando a saída
    > mais útil.

### Como Usar o Simulador

Para usar o simulador, execute o script Python em um terminal. Um menu
interativo será exibido, permitindo que você escolha as ações.

#### Iniciando o Simulador

1.  **Salve o Código:** Copie o código fornecido e salve-o em um arquivo
    > chamado hortifruti_simulador.py (ou qualquer outro nome com
    > extensão .py).

2.  **Execute o Script:** Abra seu terminal (Prompt de Comando no
    > Windows, Terminal no macOS/Linux) e navegue até o diretório onde
    > você salvou o arquivo. Em seguida, execute-o com o comando: python
    > hortifruti_simulador.py ou execute o VSCode, abra o arquivo
    > hortifruti_simulador.py e clicando F5, vai inicializar no
    > terminal.

#### Menu Principal

Ao iniciar, você verá o seguinte menu:

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
Escolha uma opção:

Digite o número correspondente à opção desejada e pressione Enter.

#### Opções do Menu Detalhadas

- **1. Listar Produtos**

  - Exibe uma lista de todos os produtos disponíveis no hortifrúti,
    > mostrando seu código, nome, preço e estoque atual. Se um produto
    > estiver em promoção, será indicado.

- **2. Cliente Chega (Montar Carrinho)**

  - Inicia a simulação de um cliente montando seu carrinho.

  - Você verá a lista de produtos novamente.

  - **Passo a passo para montar o carrinho:**

    - Digite o **código** do produto que o cliente deseja e pressione
      > Enter.

    - Se o código for válido, o sistema pedirá a **quantidade**. Digite
      > um número inteiro positivo e pressione Enter.

    - O item será adicionado ao carrinho e você poderá adicionar mais
      > produtos.

    - Para finalizar o carrinho, digite fim e pressione Enter.

  - Após montar o carrinho, o cliente será adicionado à fila do caixa.

- **3. Atender Próximo Cliente (Escanear)**

  - Remove o primeiro cliente da fila e simula o caixa escaneando os
    > produtos do carrinho.

  - O sistema verificará o estoque e aplicará promoções.

  - Será exibido o **total da compra**.

  - **Importante:** Esta opção *apenas calcula o total*. Para finalizar
    > a compra, você precisará usar a opção 4 - Processar Pagamento.

- **4. Processar Pagamento**

  - Permite que você simule o cliente pagando a compra que foi
    > \"escaneada\" na opção 3.

  - Você verá o **total a pagar**.

  - **Pagamento:** Digite o valor que o cliente está pagando (use ponto
    > . ou vírgula , para centavos, e.g., 15.75 ou 15,75) e pressione
    > Enter.

  - Se o valor for insuficiente, o sistema informará o que falta.

  - Se o valor for suficiente, o **troco** será calculado e exibido, e a
    > compra será finalizada.

  - **Atenção:** Você só pode usar esta opção se houver uma compra
    > processada pela opção 3 aguardando pagamento.

- **5. Ver Fila de Clientes**

  - Exibe quantos clientes estão aguardando na fila do caixa.

  - Também mostra uma prévia dos itens no carrinho do próximo cliente na
    > fila.

- **6. Adicionar Produto (Admin)**

  - Permite adicionar um novo produto ao catálogo do hortifrúti.

  - Você precisará informar o **código**, **nome**, **preço** e
    > **estoque inicial** do novo produto.

- **7. Remover Produto (Admin)**

  - Permite remover um produto existente do catálogo.

  - Você precisará informar o **código** do produto a ser removido.

- **8. Adicionar Promoção (Admin)**

  - Adiciona um produto à lista de promoções, aplicando um desconto
    > padrão (10% no exemplo) quando ele for escaneado.

  - Você precisará informar o **código** do produto.

- **9. Remover Promoção (Admin)**

  - Remove um produto da lista de promoções.

  - Você precisará informar o **código** do produto.

- **0. Sair**

  - Encerra o simulador.

### Exemplo de Fluxo de Uso

1.  Comece com 1 para **Listar Produtos** e ver o que está disponível.

2.  Escolha 2 para **Cliente Chega**. Digite códigos de produtos e
    > quantidades (ex: 001 e 3 para 3 bananas; 004 e 1 para 1 tomate;
    > depois fim). O cliente será adicionado à fila.

3.  Escolha 5 para **Ver Fila de Clientes** e confirme que o cliente
    > está lá.

4.  Escolha 3 para **Atender Próximo Cliente**. O sistema processará os
    > itens e mostrará o total.

5.  Escolha 4 para **Processar Pagamento**. Digite um valor pago pelo
    > cliente e veja o troco.

6.  Repita o processo com mais clientes ou explore as opções de
    > administração para adicionar/remover produtos e promoções.
