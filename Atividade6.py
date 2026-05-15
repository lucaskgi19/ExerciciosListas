pares = []
impares = []

for i in range(1,10):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

lista = pares + impares

print(f"{lista}")