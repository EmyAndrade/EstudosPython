import random

n_blusas = int(input('Quantidade de blusas: '))
n_calcas = int(input('Quantidade de calças: '))

combinacoes = []

for b in range(1, n_blusas + 1):
    for c in range(1, n_calcas + 1):
        item = f"Blusa {b} e Calça {c}"
        combinacoes.append(item)

print(f"\nTotal de looks possíveis: {len(combinacoes)}")

if combinacoes:
    look_do_dia = random.choice(combinacoes)
    print("-" * 30)
    print(f"O look escolhido é: {look_do_dia}")
    print("-" * 30)
else:
    print("A lista está vazia, não há o que sortear.")