def get_factorial(n=5):
    return n if n == 1 else n * get_factorial(n - 1)


def main():
    factorial = get_factorial()
    resp = 0
    for num in str(factorial):
        resp += int(num)
    print('\nEl factorial es: ')
    print(factorial)
    print('\nLa suma de sus dígitos es: ')
    print(resp)


if __name__ == '__main__':
    main()
