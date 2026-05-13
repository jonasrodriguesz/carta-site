# produtos cadastrados no estoque
estoque = {
    "Mouse": 10,
    "Teclado": 5,
    "Monitor": 3
}

# lista para guardar as movimentações
movimentacoes = []


# função para mostrar os produtos do estoque
def mostrar_estoque():

    print("\n===== ESTOQUE ATUAL =====")

    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")


# função para adicionar produtos no estoque
def entrada_produto():

    produto = input("Digite o nome do produto: ")

    if produto in estoque:

        quantidade = int(input("Digite a quantidade recebida: "))
        data = input("Digite a data da entrada: ")
        responsavel = input("Digite o nome do responsável: ")

        # adicionando quantidade ao estoque
        estoque[produto] += quantidade

        # salvando movimentação
        movimentacoes.append(
            f"Entrada - Produto: {produto} | Quantidade: {quantidade} | Data: {data} | Responsável: {responsavel}"
        )

        print("Entrada registrada com sucesso!")

    else:
        print("Produto não encontrado no estoque.")


# função para retirar produtos do estoque
def saida_produto():

    produto = input("Digite o nome do produto: ")

    if produto in estoque:

        quantidade = int(input("Digite a quantidade retirada: "))

        # verificando se existe quantidade suficiente
        if quantidade <= estoque[produto]:

            data = input("Digite a data da saída: ")
            responsavel = input("Digite o nome do responsável: ")

            # removendo quantidade do estoque
            estoque[produto] -= quantidade

            # salvando movimentação
            movimentacoes.append(
                f"Saída - Produto: {produto} | Quantidade: {quantidade} | Data: {data} | Responsável: {responsavel}"
            )

            print("Saída registrada com sucesso!")

        else:
            print("Erro: quantidade insuficiente no estoque.")

    else:
        print("Produto não encontrado no estoque.")


# função para mostrar movimentações realizadas
def mostrar_movimentacoes():

    print("\n===== MOVIMENTAÇÕES =====")

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")

    else:
        for item in movimentacoes:
            print(item)


# menu principal do sistema
while True:

    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Mostrar estoque")
    print("2 - Entrada de produtos")
    print("3 - Saída de produtos")
    print("4 - Mostrar movimentações")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_estoque()

    elif opcao == "2":
        entrada_produto()

    elif opcao == "3":
        saida_produto()

    elif opcao == "4":
        mostrar_movimentacoes()

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")