numConvert = input('Digite o número que você deseja converter: ')

unidadeAtual = input('Digite a unidade atual do número: ')

unidadeDesejada = input('Digite a unidade desejada para a conversão: ')

numConvert = float(numConvert)

numeroConvertido = 0
    
def comprimento(numConvert, unidade_atual, unidade_desejada):
        if unidade_atual == 'm' and unidade_desejada == 'km':
            numeroConvertido = numConvert / 1000
            print(f'{numConvert:.2f}{unidade_atual} é igual a {numeroConvertido:.2f}{unidade_desejada}.')
        
        elif unidade_atual == 'km' and unidade_desejada == 'm':
            numeroConvertido = numConvert * 1000
            print(f'{numConvert:.2f}{unidade_atual} é igual a {numeroConvertido:.2f}{unidade_desejada}.')
        
        elif unidade_atual == 'cm' and unidade_desejada == 'm':
            numeroConvertido = numConvert / 100
            print(f'{numConvert:.2f}{unidade_atual} é igual a {numeroConvertido:.2f}{unidade_desejada}.')
        
        elif unidade_atual == 'm' and unidade_desejada == 'cm':
            numeroConvertido = numConvert * 100
            print(f'{numConvert:.2f}{unidade_atual} é igual a {numeroConvertido:.2f}{unidade_desejada}.')
        
        elif unidade_atual == 'cm' and unidade_desejada == 'km':
            numeroConvertido = numConvert / 100000
            print(f'{numConvert:.2f}{unidade_atual} é igual a {numeroConvertido:.2f}{unidade_desejada}.')
        
        elif unidade_atual == 'km' and unidade_desejada == 'cm':
            numeroConvertido = numConvert * 100000
            print(f'{numConvert:.2f}{unidade_atual} é igual a {numeroConvertido:.2f}{unidade_desejada}.')
        
        else:
            print('Unidades inválidas para conversão.')

if unidadeAtual == 'm' and unidadeDesejada == 'km':
    comprimento(numConvert, unidadeAtual, unidadeDesejada)
elif unidadeAtual == 'km' and unidadeDesejada == 'm':
    comprimento(numConvert, unidadeAtual, unidadeDesejada)
elif unidadeAtual == 'cm' and unidadeDesejada == 'm':
    comprimento(numConvert, unidadeAtual, unidadeDesejada)
elif unidadeAtual == 'm' and unidadeDesejada == 'cm':
    comprimento(numConvert, unidadeAtual, unidadeDesejada)
elif unidadeAtual == 'cm' and unidadeDesejada == 'km':
    comprimento(numConvert, unidadeAtual, unidadeDesejada)
elif unidadeAtual == 'km' and unidadeDesejada == 'cm':
    comprimento(numConvert, unidadeAtual, unidadeDesejada)