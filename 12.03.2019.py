#En az sayıda madeni para kullanarak verilebilecek para üstü
def para_ustu_bulma(n, harcanan):
    coinlist = [1, 5, 10, 25]
    para_ustu = n - harcanan
    son = (len(coinlist) - 1)
    verilecek = []
    while (para_ustu != 0):
        for i in range(son, -1, -1):
            if (para_ustu >= coinlist[i]):
                a = para_ustu // coinlist[i]
                for j in range(a):
                    verilecek.append(coinlist[i])
                para_ustu = para_ustu - coinlist[i] * a

    return verilecek


def recMC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif (knownResults[change] > 0):
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:  # expression
            numCoins = 1 + recMC(coinValueList, change - i, knownResults)
            if (numCoins < minCoins):
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins


coinlist = [1, 5, 10, 25]
print(recMC(coinlist, 40, [0] * 41))
print(para_ustu_bulma(90, 43))

L_1 = [i for i in range(10)]
print(L_1)
L_2 = [i for i in range(10) if i % 2 == 0]
print(L_2)