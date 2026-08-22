estoque = [ ]

# categoria de produtos
categorias = [
    "Alimentos",
    "Bebidas",
    "Eletrônicos",
    "Limpeza",
    "Outros"
]

def cadastrar_produto():
    print('cadastrando produto')
    produto=input('digite o nome do produto: ')
    valor = float(input('digite o valor do produto: '))
    quantidade = int(input('digite a quantidade em estoque:'))

    print('categorias:')
    for codigo,categoria in enumerate(categorias,start=1):
        print(f'{codigo} - {categoria}')
    codigo_categoria = int(input('digite categoria do produto:'))
    if codigo_categoria < 1 or codigo_categoria > len(categorias):
        print("Categoria inválida!")
        return

    categoria = categorias[codigo_categoria -1]


    produto=[produto,valor,quantidade,categoria]
      # Adicionando o produto na lista estoque
    estoque.append(produto)

    print('produto cadastrado:')

# função
def listar_produtos():

    if len(estoque) == 0:
        print('estoque vazio:')
        return

    for  codigo,produto in enumerate ( estoque, start=1):
        print(f'codigo: {codigo}')
        print(f'produto: {produto[0]}')
        print(f'valor: {produto[1]}')
        print(f'quantidade: {produto[2]}')
        print(f'categoria: {produto[3]}')


    #função
def consultar_produto():

    buscar_produto = input('digite nome do produto: ')

    for produto in estoque:
        if produto[0].lower() == buscar_produto.lower():

            print('produto encontrado!')
            print(f'nome: {produto[0]}')
            print(f'valor: {produto[1]}')
            print(f'quantidade: {produto[2]}')
            print(f'categoria:{produto[3]}')
            print('produto nao encontrado!')

            return


       # função
def alterar_produto():
    nova_categoria = input('digite nova categoria!')
            produto[3]=nova_categoria
    buscar_produto = input ("digite o nome do produto que deseja alterar:")

    for produto in estoque:
        if produto[0].lower() == buscar_produto.lower():
            print('produto encontrado!')

            nome_novo = input('digite novo nome: ')
            novo_valor = float(input('digite novo valor: '))
            nova_quantidade = int(input('digite nova quantidade: '))

            print('Categorias:')
            for codigo, categoria in enumerate(categorias, start=1):
                print(f'{codigo} - {categoria}')

            codigo_categoria = int(input("Escolha a nova categoria: "))

            if codigo_categoria < 1 or codigo_categoria > len(categorias):
                print('Categoria inválida!')
                return

                nova_categoria = categorias[codigo_categoria-1]
a
            produto[0]=nome_novo
            produto[1]=novo_valor
            produto[2]=nova_quantidade
            produto[3]=nova_categoria


            print('produto alterado! ')

            return

    print('produto nao encontrado! ')

          # função
def excluir_produto():

    buscar_produto = input('digite o nome: ')
    for produto in estoque:

        if produto[0].lower() == buscar_produto.lower():

           estoque.remove(produto)
           print('produto excluido! ')

           return
    print('produto nao encontrado!')

 #funçao
def salvar_estoque():
    with open('estoque.txt','w', encoding='utf-8') as arquivo:
        for produto in estoque:
            arquivo.write(
                f'produto: {produto[0]}\n'
                f'valor: {produto[1]}\n'
                f'quantidade: {produto[2]}\n'
                f'categoria: {produto[3]}\n'

            )
    print('estoque salvo!')

    #menu

while True:

    print('1 - cadastrar produto')
    print('2- listar produtos')
    print('3- consultar_produto')
    print('4- alterar_produto')
    print('5- excluir_produto')
    print('6- salvar_estoque')
    print('0- sair')

    opcao = input('digite sua opcao: ')

    if opcao == '1':
        cadastrar_produto()
    elif opcao =='2':
        listar_produtos()
    elif opcao =='3':
        consultar_produto()
    elif opcao =='4':
        alterar_produto()
    elif opcao == '5':
        excluir_produto()
    elif opcao =='6':
        salvar_estoque()
    elif opcao =='0':
        print('sair')

        break
    else:
        print('opcao invalida!')
