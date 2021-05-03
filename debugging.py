def divisors(num):
    try:
        if num < 0 or num == 0:
            raise ValueError('Ingresa un numero mayor a cero')
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        return ve

def main():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisors(num))
        print('Ok...')
    except ValueError:
        print('Debes ingresar un numero entero')


if __name__ == '__main__':
    main()