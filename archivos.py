def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Leo', 'Facundo', 'Lola', 'Selena', 'Iván']
    with open("./files/names.txt", "w", encoding="utf-8") as f: #Parametro w sobreescribe el archivo
    # with open("./files/names.txt", "a", encoding="utf-8") as f: #Parametro a escribe añadiendo al final al achivo
        for name in names:
            f.write(name)
            f.write('\n')


def main():
    write()


if __name__ == '__main__':
    main()