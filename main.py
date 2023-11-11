creditos_clientes = {}

catalogo_itens = {
    "Banana": 10,
    "Maçã": 20,
    "Laranja": 15,
    "Maracuja": 30,
    "Melancia": 25
}

def atribuir_creditos(cliente, valor_creditos):
    if cliente in creditos_clientes:
        creditos_clientes[cliente] += valor_creditos
    else:
        creditos_clientes[cliente] = valor_creditos

def consultar_creditos(cliente):
    if cliente in creditos_clientes:
        return creditos_clientes[cliente]
    else:
        return 0

def trocar_itens(cliente, itens_para_troca):
    total_creditos = sum(catalogo_itens[item] for item in itens_para_troca)
    if cliente in creditos_clientes and creditos_clientes[cliente] >= total_creditos:
        for item in itens_para_troca:
            creditos_clientes[cliente] -= catalogo_itens[item]
        print(f"Troca realizada com sucesso! Novo saldo de créditos de {cliente}: {creditos_clientes[cliente]}")
    else:
        print("Saldo de créditos insuficiente para realizar a troca.")

def visualizar_catalogo():
    print("Catálogo de Itens Disponíveis:")
    for item, valor in catalogo_itens.items():
        print(f"{item}: {valor} créditos")

if __name__ == "__main__":
    while True:
        print("Opções:")
        print("1. Atribuir créditos a um cliente (Funcionários)")
        print("2. Consultar créditos de um cliente (Funcionários)")
        print("3. Visualizar catálogo de itens disponíveis (Clientes)")
        print("4. Realizar troca de itens (Clientes)")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = input("Informe o nome do cliente: ")
            valor_creditos = float(input("Informe o valor dos créditos a serem atribuídos: "))
            atribuir_creditos(cliente, valor_creditos)
            print(f"Créditos atribuídos com sucesso! Créditos totais de {cliente}: {consultar_creditos(cliente)}")
        elif opcao == "2":
            cliente = input("Informe o nome do cliente: ")
            creditos = consultar_creditos(cliente)
            print(f"Créditos de {cliente}: {creditos}")
        elif opcao == "3":
            visualizar_catalogo()
        elif opcao == "4":
            cliente = input("Informe o nome do cliente: ")
            visualizar_catalogo()
            itens_para_troca = input("Informe os itens desejados para troca (separados por vírgula): ").split(",")
            trocar_itens(cliente, itens_para_troca)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
