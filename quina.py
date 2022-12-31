import random
cartelas = list(range(0, 100))
for i in range(0, 100):
    cartela = random.randint(1, 24040016)
    cartelas[i] = cartela
print(cartelas)
jogo = 0
for a in range(0, 80):
    for b in range(a+1, 80):
        for c in range(b+1, 80):
            for d in range(c+1, 80):
                for e in range(d+1, 80):
                    jogo = jogo+1
                    for x in range(0, 100):
                        if (jogo == cartelas[x]):
                            print(str(jogo) + ' ' + str(a+1) + ' ' + str(b+1) +
                                  ' ' + str(c+1) + ' ' + str(d+1) + ' ' + str(e+1))

print("Percorri no processo filho 24.040.016 combinações que correspondem a combinação de 80, 5 a 5")
