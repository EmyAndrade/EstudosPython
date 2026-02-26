import os

lista = []

while True:
    print('Digite uma opção:')
    opcao = input('[i]nserir, [l]istar, [a]pagar, [s]air: ').lower()

    if opcao == 'i':
        item = input('Digite o item a ser adicionado à lista: ')
        lista.append(item)
        print(f'Item "{item}" adicionado à lista.')

    elif opcao == 'l':
        if not lista:
            print('A lista está vazia.')
        else:
            print('Itens na lista:')
            for index, item in enumerate(lista, start=1):
                print(f'{index}. {item}')

    elif opcao == 'a':
        if not lista:
            print('A lista está vazia.')
        else:
            print('Itens na lista:')
            for index, item in enumerate(lista, start=1):
                print(f'{index}. {item}')
            try:
                indice = int(input('Digite o número do item a ser removido: ')) - 1
                if 0 <= indice < len(lista):
                    item_removido = lista.pop(indice)
                    print(f'Item "{item_removido}" removido da lista.')
                else:
                    print('Índice inválido.')
            except ValueError:
                print('Digite um número válido.')

    elif opcao == 's':
        print('Encerrando o programa.')
        break

    else:
        print('Opção inválida.')