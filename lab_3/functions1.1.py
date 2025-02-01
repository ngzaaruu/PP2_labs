def grams_to_ounces (g):
    o = g / 28.3495231
    return o

g = float(input())
o = grams_to_ounces(g)

#print(g, " grams ", "= ", o, " ounces " )

print(g, "grams =", round(o, 3), "ounces")