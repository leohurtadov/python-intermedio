def divisors(num):
    assert num != 0, 'Debes ingresar un numero mayor a cero'
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def main():
    num = input('Ingresa un numero: ')
    assert num.isnumeric(), 'Ingresa un numero entero'
    print(divisors(int(num)))
    print('Listo')


if __name__ == '__main__':
    main()