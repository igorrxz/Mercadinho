
catalogo_itens = {
    "Banana": 10,
    "Maçã": 20,
    "Laranja": 15,
    "Maracuja": 30,
    "Melancia": 25
}

def visualizar_catalogo():
    print("Catálogo de Itens Disponíveis:")
    for item, valor in catalogo_itens.items():
        print(f"{item}: {valor} créditos")

if __name__ == "__main__":
    while True:
        print("Opções:")
        print("1. Visualizar catálogo de itens disponíveis")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_catalogo()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
