def escaliers(n):
    if n <= 1:
        return 1
    return escaliers(n-1) + escaliers(n-2)

print("Escaliers 4 =", escaliers(4))


def compter_mots(texte):
    mots = texte.split()
    return len(mots)

print("Nombre de mots =", compter_mots("Bonjour tout le monde, commencez à coder."))
