produtos=[ ]

print(produtos)
while True:
    produto =input("Digite o nome do produto:")

    if produto =="sair":
        print(produtos)
        break
    elif produto == "sair":
        print(produtos)
        break

    elif produto == "remover":
        produto_remover =input("digite o nome do produto que deseja remover:")
        produtos.remove(produto_remover)

    else:
        produtos.append(produto)
     print(produtos)




    if produto == ("remover"):
        produto_remover = input("Digite o nome do produto:")
        produtos.remove(produto_remover)

