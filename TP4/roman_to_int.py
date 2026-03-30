def roman_to_int(s):
    valeurs = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 0

    for c in reversed(s):
        val = valeurs[c]

        if val < prev:
            total -= val
        else:
            total += val

        prev = val

    return total


def int_to_roman(num):
    valeurs = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    resultat = ""

    for val, sym in valeurs:
        while num >= val:
            resultat += sym
            num -= val

    return resultat


print("1 - Romain vers entier")
print("2 - Entier vers romain")

choix = input("Choix : ")

if choix == "1":
    roman = input("Entrer un nombre romain : ")
    print("Valeur entière :", roman_to_int(roman))

elif choix == "2":
    entier = int(input("Entrer un entier : "))
    print("Nombre romain :", int_to_roman(entier))

else:
    print("Choix invalide")
