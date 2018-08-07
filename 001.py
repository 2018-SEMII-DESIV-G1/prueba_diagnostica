def get_fib_series(n=10):
    # Secuencia regular fibonacci
    fib = [0, 1]

    # Secuencia de fibonacci sólo con impares
    resfib = [0, 1]
    
    # El i empieza en 2 porque estoy ignorando los 2
    # primeros elementos del array "fib", ya que
    # siempre son 0 y 1.
    i = 2

    # Mientras la cantidad de elementos en resfib
    # sea menor que la cantidad de elementos que buscamos
    while(len(resfib) < n):
        # Calculamos fib
        _n = (fib[i - 2] + fib[i - 1])
        if(_n % 2 != 0):
            # Solo añadimos a este array si el elemento es impar
            resfib.append(_n)
        # Seguimos añadiendo siempre a la secuencia
        fib.append(_n)
        # Incrementamos el contador de elementos de toda la 
        # serie fibonacci.
        i += 1
    return resfib, fib

def main():
    resfib, fib = get_fib_series()
    resultado = 0
    for number in resfib:
        resultado += number
    print('\nEl arreglo con elementos de fibonacci impares: ')
    print(resfib)
    print('\nEl arreglo con todos los elementos de fibonacci: ')
    print(fib)
    print('\nEl resultado de la suma de todos los elementos '
          'impares es de: ' + str(resultado))

if __name__ == '__main__':
    main()