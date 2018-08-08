def main():
    cadena = input('Introduzca la cadena: ')
    if (cadena == cadena[::-1]):
	    print('La cadena es un palindromo')
    else:
        print('La cadena no es un palindromo')

if __name__ == '__main__':
    main()
