print("Bem-vindo à nossa loja!!")

nome = input("Qual é o seu nome: ")
saldo = float(input("Quanto tem para gastar?: "))

# dicionário com produtos e preços
produtos = {
    "água": 2.50,
    "cerveja": 5.00,
    "refrigerante": 4.00
}

# histórico de compras
carrinho = {}
extrato = []

def acrescentar_produto():
    produto = input("Digite o nome do produto: ").lower()
    try:
        preco = float(input("Digite o preço do produto: "))
        if preco <= 0:
            print("O preço deve ser maior que zero.")
            return
        produtos[produto] = preco
        print(f"Produto '{produto}' adicionado com sucesso!")
    except ValueError:
        print("Preço inválido!")

def exibir_produtos():
    print("\nProdutos disponíveis:")
    for item, preco in produtos.items():
        print(f"- {item.capitalize()} → R$ {preco:.2f}")

def comprar(saldo):
    exibir_produtos()
    produto = input("\nDigite o nome do produto: ").lower()
    
    if produto not in produtos:
        print("Produto inválido!")
        return saldo
    
    try:
        quantidade = int(input(f"Quantas unidades de {produto} você deseja comprar? "))
        if quantidade <= 0:
            print("Quantidade inválida!")
            return saldo
    except ValueError:
        print("Digite um número válido para a quantidade.")
        return saldo

    total = produtos[produto] * quantidade
    
    if saldo >= total:
        saldo -= total
        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        extrato.append(f"Compra: {quantidade}x {produto.capitalize()} → -R$ {total:.2f}")
        print(f"\n✅ Compra realizada! Você comprou {quantidade} {produto}(s) por R$ {total:.2f}.")
        print(f"💰 Seu saldo agora é: R$ {saldo:.2f}")
    else:
        print("❌ Saldo insuficiente!")
    
    return saldo

def remover_produto(saldo):
    if not carrinho:
        print("Seu carrinho está vazio!")
        return saldo
    
    print("\nProdutos no carrinho:")
    for item, qtd in carrinho.items():
        print(f"- {item.capitalize()} (quantidade: {qtd})")
    
    produto = input("Digite o nome do produto que deseja remover: ").lower()
    
    if produto not in carrinho:
        print("Esse produto não está no carrinho.")
        return saldo
    
    try:
        quantidade = int(input(f"Quantas unidades de {produto} deseja remover? "))
        if quantidade <= 0 or quantidade > carrinho[produto]:
            print("Quantidade inválida!")
            return saldo
    except ValueError:
        print("Digite um número válido.")
        return saldo
    
    total = produtos[produto] * quantidade
    carrinho[produto] -= quantidade
    if carrinho[produto] == 0:
        del carrinho[produto]
    
    saldo += total
    extrato.append(f"Devolução: {quantidade}x {produto.capitalize()} → +R$ {total:.2f}")
    print(f"\n🔄 Você devolveu {quantidade} {produto}(s).")
    print(f"💰 Seu saldo agora é: R$ {saldo:.2f}")
    
    return saldo

def ver_extrato(saldo):
    print("\n=== EXTRATO DA CONTA ===")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for mov in extrato:
            print(mov)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("========================")

def resumo_final(saldo):
    print("\n=== RESUMO DAS COMPRAS ===")
    if not carrinho:
        print("Você não comprou nada.")
    else:
        for item, qtd in carrinho.items():
            print(f"- {qtd}x {item.capitalize()} → R$ {produtos[item] * qtd:.2f}")
    print("==========================")
    print(f"Saldo final: R$ {saldo:.2f}")
    print("Obrigado por comprar conosco!")

# 👉 Função de forma de pagamento
def forma_pagamento(total):
    print("\n=== FORMAS DE PAGAMENTO ===")
    print("[1] Dinheiro")
    print("[2] Cartão")
    print("[3] Pix")
    
    escolha = input("Escolha a forma de pagamento: ")
    
    if escolha == "1":
        print("💵 Pagamento em dinheiro selecionado.")
        try:
            valor = float(input("Digite o valor entregue: R$ "))
            if valor < total:
                print("⚠️ Valor insuficiente!")
            elif valor == total:
                print("✅ Pagamento realizado sem troco.")
            else:
                troco = valor - total
                print(f"✅ Pagamento realizado. Seu troco é R$ {troco:.2f}.")
        except ValueError:
            print("Entrada inválida!")
    
    elif escolha == "2":
        print("💳 Pagamento em cartão realizado com sucesso.")
    
    elif escolha == "3":
        print("📱 Pagamento via Pix realizado com sucesso.")
    
    else:
        print("Opção inválida.")

def exibir_menu(saldo):
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("[1] Consultar produtos disponíveis")
        print("[2] Comprar")
        print("[3] Adicionar produto")
        print("[4] Remover produto do carrinho")
        print("[5] Ver extrato")
        print("[6] Finalizar compra e pagar")
        print("[0] Sair")
        
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue
        
        if escolha == 1:
            exibir_produtos()
        elif escolha == 2:
            saldo = comprar(saldo)
        elif escolha == 3:
            acrescentar_produto()
        elif escolha == 4:
            saldo = remover_produto(saldo)
        elif escolha == 5:
            ver_extrato(saldo)
        elif escolha == 6:
            total_compras = sum(produtos[item] * qtd for item, qtd in carrinho.items())
            if total_compras > 0:
                forma_pagamento(total_compras)
                resumo_final(saldo)
                break
            else:
                print("⚠️ Seu carrinho está vazio.")
        elif escolha == 0:
            resumo_final(saldo)
            ver_extrato(saldo)
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

exibir_menu(saldo)
