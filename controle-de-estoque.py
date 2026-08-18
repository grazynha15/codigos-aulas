produtos = []

while True:
    produto = input("Digite o nome do produto:")

    if produto == "sair":
        print(produtos)
        break
    elif produto == "sair":
        produto_remover=input("digite o nome do produto que deseja remover:")
        produtos.remove(produto_remover)

    else:
        produtos.append(produto)
    print(produtos)




