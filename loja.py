








# 1 - Adicionaar
# 2 - Exibir detalhes
# 3 - Atualizar
# 4 - Apagar
# 5 - Exibir todos


lista_produtos = []

def menu():
    while True:
        print('\n ** MENU LOJA REPROGRAMA **\n')
        print('1 - Adicionar')
        print('2 - Exibir detalhes')
        print('3 - Atualizar')
        print('4 - Apagar')
        print('5 - Exibir todos')
        print('0 - Sair')

        opcao = input('Escolha a opção desejada:\n')

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            print('Opcão exibier detalhes doce')
        elif opcao == '3':
            print('Opcão atualizar doce')
        elif opcao == '4':
            print('Opção apagar doce')
        elif opcao == '5':
            print('Opção exibir todos os doces')
        elif opcao == '0':
            break
        else:
            print('Opção inválida, por favor escolha uma opção do menu')