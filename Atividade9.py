import random
alfabeto = [["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"], ["m"], ["n"], ["o"], ["p"], ["q"], ["r"], ["s"], ["t"], ["u"], ["v"], ["w"], ["x"], ["y"], ["z"]]
random.shuffle(alfabeto)
print(alfabeto)
letra = random.choice(alfabeto)
num = input("informe a posicao da letra:") 
indice = alfabeto.index(letra)
print(indice)
print(f"A letra '{letra}' está na posição {indice}")

if num == letra:
    print("voce acertou a posicao da letra")
else:
    print("Voce errou a posicao")
