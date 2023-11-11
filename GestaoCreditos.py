creditos_clientes = {}

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

if __name__ == "__main__":
    while True:
        print("Opções:")
        print("1. Atribuir créditos a um cliente")
        print("2. Consultar créditos de um cliente")
        print("3. Sair")
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
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
