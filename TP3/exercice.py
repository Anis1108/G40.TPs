def somme_nulle_deux(t):
    result = []
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] + t[j] == 0:
                result.append([t[i], t[j]])
    return result


def somme_nulle_trois(t):
    result = []
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            for k in range(j + 1, len(t)):
                if t[i] + t[j] + t[k] == 0:
                    result.append([t[i], t[j], t[k]])
    return result


t = [1, 20, 15, 3, 5, -3, 41]

print(somme_nulle_deux(t))
print(somme_nulle_trois(t))
