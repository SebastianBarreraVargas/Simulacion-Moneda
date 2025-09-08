import random

def simular_moneda(lado):
    lanzamientos = [1, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    probabilidades = []

    for n in lanzamientos:
        favorables = 0

        for _ in range(n):
            resultado = random.randint(0, 1)
            if resultado == lado:
                favorables += 1

        probabilidad = (favorables / n) * 100
        probabilidades.append(probabilidad)

    return tuple(probabilidades), lanzamientos