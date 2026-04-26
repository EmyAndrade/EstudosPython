perguntas = [
    {
        'pergunta' : 'Quantos que é 2 + 2?',
        'opções' : ['1', '2', '3', '4'],
        'resposta' : '4'
    },

    {
        'pergunta' : 'Quantos que é 5 * 5?',
        'opções' : ['25', '10', '15', '20'],
        'resposta' : '25'
    },

    {
        'pergunta' : 'Quantos que é 4 / 2?',
        'opções' : ['10', '8', '2', '0'],
        'resposta' : '2'
    }
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['pergunta'])
    print()

    opcoes = pergunta['opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')