import re
import sys

cpfdigitado = input("Digite o CPF (somente números): ")
cpfformatado = re.sub(r'[^0-9]', '', cpfdigitado)


cpfdigitado_sequencial = cpfformatado == cpfformatado[0] * len(cpfformatado)

if cpfdigitado_sequencial:
    print("CPF inválido: sequência de números repetidos.")
    sys.exit()

nove_digitos = cpfformatado[:9]
contagem_regressiva = 10
multiplicacao = 0

for digito in nove_digitos:
    multiplicacao += int(digito) * contagem_regressiva
    contagem_regressiva -= 1
    digito_1 = (multiplicacao * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpfformatado == cpf_gerado_pelo_calculo:
    print(f'{cpfformatado} é válido')
else:
    print('CPF inválido')