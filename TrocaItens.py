
catalogo_itens = {
    "Banana": 10,
    "Maçã": 20,
    "Laranja": 15,
    "Maracuja": 30,
    "Melancia": 25
}

creditos_clientes = {
    "Igor": 50,
    "Yuri": 30,
    "Eduardo": 70
}

def trocar_itens(cliente, itens_para_troca):
    total_creditos = sum(catalogo_itens[item] for item in itens_para_troca)
    if cliente in creditos_clientes and creditos_clientes[cliente] >= total_creditos:
        for item in itens_para_troca:
            creditos_clientes[cliente] -= catalogo_itens[item]
        print(f"Troca realizada com sucesso! Novo saldo de créditos de {cliente}: {creditos_clientes[cliente]}")
    else:
        print("Saldo de créditos insuficiente para realizar a troca.")

# Exemplo de uso
if __name__ == "__main__":
    while True:
        print("Opções:")
        print("1. Realizar troca de itens")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = input("Informe o nome do cliente: ")
            visualizar_catalogo()
            itens_para_troca = input("Informe os itens desejados para troca (separados por vírgula): ").split(",")
            trocar_itens(cliente, itens_para_troca)
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
