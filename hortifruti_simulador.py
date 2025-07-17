from collections import deque

class Hortifruti:
    def __init__(self):
        self.produtos = {
            '001': {'produto': 'Banana (palma)', 'preco': 1.50, 'estoque': 20},
            '002': {'produto': 'Maçã (kg)', 'preco': 2.00, 'estoque': 50},
            '003': {'produto': 'Laranja (kg)', 'preco': 1.80, 'estoque': 75},
            '004': {'produto': 'Tomate (kg)', 'preco': 3.00, 'estoque': 30},
            '005': {'produto': 'Cenoura (kg)', 'preco': 2.50, 'estoque': 60},
            '006': {'produto': 'Batata (kg)', 'preco': 1.20, 'estoque': 80},
            '007': {'produto': 'Alface (kg)', 'preco': 1.00, 'estoque': 40},
            '008': {'produto': 'Pepino (kg)', 'preco': 1.70, 'estoque': 55},
            '009': {'produto': 'Cebola (kg)', 'preco': 1.30, 'estoque': 90},
            '010': {'produto': 'Pimentão (kg)', 'preco': 2.20, 'estoque': 20},
            '011': {'produto': 'Abobora (kg)', 'preco': 1.60, 'estoque': 45},
            '012': {'produto': 'Berinjela (kg)', 'preco': 2.40, 'estoque': 35},
            '013': {'produto': 'Brócolis (kg)', 'preco': 2.80, 'estoque': 25},
            '014': {'produto': 'Espinafre (kg)', 'preco': 1.90, 'estoque': 65},
            '015': {'produto': 'Repolho (kg)', 'preco': 1.40, 'estoque': 70},
            '016': {'produto': 'Inhame (kg)', 'preco': 6.15, 'estoque': 50},
            '017': {'produto': 'Couve-flor (kg)', 'preco': 2.30, 'estoque': 30},
            '018': {'produto': 'Melancia (kg)', 'preco': 1.75, 'estoque': 55},
            '019': {'produto': 'Macaxeira (kg)', 'preco': 1.85, 'estoque': 40},
            '020': {'produto': 'Batata-doce (kg)', 'preco': 1.95, 'estoque': 60},
        }
        self.fila_clientes = deque()
        self.produtos_em_promocao = {'001', '003', '005'} # Banana, Laranja, Cenoura em promoção!
        self.historico_caixa = [] # Pilha para um futuro "desfazer"
        self.total_compra_atual = 0.0 # Armazena o total da compra do cliente atualmente em atendimento
        self.carrinho_em_processo = [] # Armazena os itens comprados (com sucesso) do cliente atual

    def listar_produtos(self): # função para listar os produtos disponíveis
        print("\n--- Produtos Disponíveis ---")
        for codigo, detalhes in self.produtos.items():
            status_promo = "(PROMOÇÃO!)" if codigo in self.produtos_em_promocao else ""
            print(f"Código: {codigo} | Produto: {detalhes['produto']:<15} | Preço: R${detalhes['preco']:.2f} | Estoque: {detalhes['estoque']} {status_promo}")
        print("----------------------------")

    def adicionar_produto(self, codigo, nome, preco, estoque_inicial=0): # função para adicionar um novo produto
        if codigo not in self.produtos:
            self.produtos[codigo] = {'produto': nome, 'preco': preco, 'estoque': estoque_inicial}
            print(f"Produto '{nome}' (Código: {codigo}) adicionado com sucesso.")
        else:
            print(f"Erro: Produto com código {codigo} já existe.")

    def remover_produto(self, codigo): # função para remover um produto existente
        if codigo in self.produtos:
            nome_produto = self.produtos[codigo]['produto']
            del self.produtos[codigo]
            print(f"Produto '{nome_produto}' (Código: {codigo}) removido com sucesso.")
        else:
            print(f"Erro: Produto com código {codigo} não encontrado.")

    def adicionar_cliente_a_fila(self, carrinho_cliente): # função para adicionar um cliente à fila
        self.fila_clientes.append(carrinho_cliente)
        print(f"Cliente adicionado à fila com {len(carrinho_cliente)} itens.")

    def atender_proximo_cliente(self): # função para atender o próximo cliente na fila
        if not self.fila_clientes:
            print("Não há clientes na fila.")
            return False # Indica que não há cliente para atender

        # Limpa os dados da compra anterior
        self.total_compra_atual = 0.0
        self.carrinho_em_processo = []

        carrinho_do_cliente = self.fila_clientes.popleft() # Cliente retirado da fila
        print(f"\n--- Atendendo novo cliente ---")
        
        for item_codigo, quantidade_desejada in carrinho_do_cliente:
            if item_codigo in self.produtos:
                detalhes_produto = self.produtos[item_codigo]
                nome_produto = detalhes_produto['produto']
                preco_unitario = detalhes_produto['preco']
                estoque_atual = detalhes_produto['estoque']

                if item_codigo in self.produtos_em_promocao:
                    preco_unitario *= 0.90 # Exemplo: 10% de desconto
                    print(f"  Promoção aplicada a {nome_produto}!")

                if estoque_atual >= quantidade_desejada:
                    custo_item = preco_unitario * quantidade_desejada
                    self.total_compra_atual += custo_item
                    self.produtos[item_codigo]['estoque'] -= quantidade_desejada
                    # Armazena os itens processados no carrinho_em_processo
                    self.carrinho_em_processo.append((nome_produto, quantidade_desejada, preco_unitario))
                    print(f"  Adicionado: {quantidade_desejada}x {nome_produto} (R${custo_item:.2f})")
                else:
                    print(f"  Estoque insuficiente para {nome_produto}. Desejado: {quantidade_desejada}, Disponível: {estoque_atual}. Não adicionado.")
            else:
                print(f"  Produto com código {item_codigo} não encontrado no catálogo.")
        
        if self.total_compra_atual > 0: # Verifica se há itens válidos na compra
            print(f"\n--- Total da Compra: R${self.total_compra_atual:.2f} ---")
            print("Pronto para pagamento.")
            return True # Indica que há uma compra para pagar
        else:
            print("Nenhum item foi comprado ou estoque insuficiente. Cliente dispensado.")
            return False # Indica que não há compra para pagar

    def processar_pagamento(self): # função para processar o pagamento
        if self.total_compra_atual <= 0:
            print("Não há uma compra ativa para ser paga. Atenda um cliente primeiro.")
            return False

        print(f"\n--- Processando Pagamento ---")
        print(f"Total a pagar: R${self.total_compra_atual:.2f}")

        while True:
            try:
                valor_pago_str = input("Valor pago pelo cliente: R$ ").replace(',', '.').strip()
                valor_pago = float(valor_pago_str)
                
                if valor_pago < self.total_compra_atual:
                    print(f"Valor insuficiente. Faltam R${self.total_compra_atual - valor_pago:.2f}")
                else:
                    troco = valor_pago - self.total_compra_atual
                    print(f"Pagamento recebido: R${valor_pago:.2f}")
                    print(f"Troco: R${troco:.2f}")
                    print("Compra finalizada com sucesso!\n")
                    
                    # Adiciona a transação ao histórico (pilha)
                    self.historico_caixa.append({
                        'tipo': 'venda',
                        'total': self.total_compra_atual,
                        'itens': self.carrinho_em_processo, # Itens que realmente foram vendidos
                        'pago': valor_pago,
                        'troco': troco
                    })
                    
                    # Reseta o total da compra e o carrinho em processo para o próximo cliente
                    self.total_compra_atual = 0.0
                    self.carrinho_em_processo = []
                    return True # Pagamento bem-sucedido
            except ValueError:
                print("Valor inválido. Digite um número para o pagamento.")

    def ver_fila_clientes(self): # função para ver a fila de clientes
        print(f"Clientes na fila: {len(self.fila_clientes)}")
        if self.fila_clientes: # Mostra o primeiro carrinho da fila para pré-visualização
            carrinho_preview = ", ".join([f"{qtd}x {self.produtos[cod]['produto']}" for cod, qtd in self.fila_clientes[0] if cod in self.produtos])
            print(f"Próximo cliente com carrinho de: [{carrinho_preview}]")
        else:
            print("A fila está vazia.")

    def adicionar_promocao(self, codigo_produto): # função para adicionar um produto à promoção
        if codigo_produto in self.produtos:
            self.produtos_em_promocao.add(codigo_produto)
            print(f"Produto '{self.produtos[codigo_produto]['produto']}' adicionado às promoções.")
        else:
            print(f"Erro: Produto com código {codigo_produto} não existe para adicionar à promoção.")

    def remover_promocao(self, codigo_produto): # função para remover um produto da promoção
        if codigo_produto in self.produtos_em_promocao:
            self.produtos_em_promocao.remove(codigo_produto)
            print(f"Produto '{self.produtos[codigo_produto]['produto']}' removido das promoções.")
        else:
            print(f"Erro: Produto com código {codigo_produto} não está em promoção.")

    def simular_cliente_montando_carrinho(self):   # Função para simular um cliente montando seu carrinho de compras
        carrinho_do_cliente = []
        print("\n--- Montando o Carrinho de Compras ---")
        self.listar_produtos() # Mostra os produtos disponíveis
        
        while True:
            codigo = input("Digite o CÓDIGO do produto (ou 'fim' para terminar): ").strip()
            if codigo.lower() == 'fim':
                break

            if codigo not in self.produtos:
                print("Código de produto inválido. Tente novamente.")
                continue

            try:
                quantidade_str = input(f"Digite a QUANTIDADE de '{self.produtos[codigo]['produto']}': ").strip()
                quantidade = int(quantidade_str)
                if quantidade <= 0:
                    print("Quantidade deve ser um número positivo. Tente novamente.")
                    continue
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro. Tente novamente.")
                continue
            
            # Adiciona o item como uma tupla (código, quantidade) ao carrinho
            carrinho_do_cliente.append((codigo, quantidade))
            print(f"'{self.produtos[codigo]['produto']}' x{quantidade} adicionado ao carrinho.")
        
        print(f"\nCarrinho finalizado com {len(carrinho_do_cliente)} itens.")
        return carrinho_do_cliente

if __name__ == "__main__":
    supermercado = Hortifruti() 
    cliente_atendido_para_pagar = False # Flag para controlar se há um cliente para pagar
    
    print("\n===== Hortifruti Sensação =====")
    print("1. Listar Produtos")
    print("2. Cliente Chega (Montar Carrinho)")
    print("3. Atender Próximo Cliente (Escanear)")
    print("4. Processar Pagamento") 
    print("5. Ver Fila de Clientes")
    print("6. Adicionar Produto (Admin)")
    print("7. Remover Produto (Admin)")
    print("8. Adicionar Promoção (Admin)")
    print("9. Remover Promoção (Admin)")
    print("0. Sair")
    print("========================================")

    while True:
        escolha = input("Escolha uma opção: ").strip() # Input do usuário

        if escolha == '1':
            supermercado.listar_produtos()
        elif escolha == '2':
            novo_carrinho = supermercado.simular_cliente_montando_carrinho()
            if novo_carrinho:
                supermercado.adicionar_cliente_a_fila(novo_carrinho)
        elif escolha == '3':
            # Se atender_proximo_cliente retornar True, significa que há uma compra para pagar
            cliente_atendido_para_pagar = supermercado.atender_proximo_cliente()
        elif escolha == '4': # Nova opção de pagamento
            if cliente_atendido_para_pagar:
                supermercado.processar_pagamento()
                cliente_atendido_para_pagar = False # Reseta a flag após o pagamento
            else:
                print("Não há clientes na fila de pagamento. Atenda um cliente primeiro (Opção 3).")
        elif escolha == '5':
            supermercado.ver_fila_clientes()
        elif escolha == '6':
            codigo = input("Código do novo produto: ").strip()
            nome = input("Nome do novo produto: ").strip()
            try: 
                preco_str = input("Preço do novo produto: ").replace(',', '.').strip()
                preco = float(preco_str)
                estoque_str = input("Estoque inicial do novo produto: ").strip()
                estoque = int(estoque_str)
                supermercado.adicionar_produto(codigo, nome, preco, estoque)
            except ValueError:
                print("Entrada inválida para preço ou estoque.")
        elif escolha == '7':
            codigo = input("Código do produto a remover: ").strip()
            supermercado.remover_produto(codigo)
        elif escolha == '8':
            codigo = input("Código do produto para adicionar à promoção: ").strip()
            supermercado.adicionar_promocao(codigo)
        elif escolha == '9':
            codigo = input("Código do produto para remover da promoção: ").strip()
            supermercado.remover_promocao(codigo)
        elif escolha == '0': 
            print("Saindo do simulador. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")