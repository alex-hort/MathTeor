def cribado_eratostenes(n):
    """
    Implementación del Cribado de Eratóstenes
    """
    total=0
    # Creamos una lista con todos los números del 2 al n
    numeros = list(range(2, n+1))
    # Iniciamos el cribado
    for i in numeros:
        # Si el número ya ha sido marcado como no primo, saltamos a la siguiente iteración
        if i is None:
            continue
        # Si el número es primo, marcamos todos sus múltiplos como no primos
        total+=1
        for j in range(i*2, n+1, i):
            numeros[j-2] = None

    # Devolvemos una lista con los números primos encontrados
    return total,[num for num in numeros if num is not None]

def imprimir_factores_primos(n):
    # Comience con dos, que es el primer primo
    factor = 2
    Asx = []
    # Continúe hasta que el factor sea mayor que el número
    while factor <= n:
    # Verificar si el factor es un divisor de número
        if not (n % factor != 0):
        # Si es así, imprímalo y divida el número original
            Asx.append(factor)
            n /= factor
        else:
        # Si no es así, incremente el factor en uno
            factor += 1


    return Asx

# Encontramos los primeros números primos

x = input("Escribe un numero")
x = int(x)
total,primos = cribado_eratostenes(x)

factor = imprimir_factores_primos(x)
# Imprimimos los resultados
print(f"Total de números encontrados {total}\nLos números primos son: {primos}\nLos factores son: {factor}")