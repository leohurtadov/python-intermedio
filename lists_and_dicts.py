def main():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Leonardo','lastname': 'Hurtado'}
    
    super_list = [
        {'firstname': 'Leonardo', 'lastname': 'Hurtado'},
        {'firstname': 'Miguel', 'lastname': 'Torres'},
        {'firstname': 'Pepe', 'lastname': 'Nacho'},
        {'firstname': 'Sara', 'lastname': 'Laru'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 6],
        'floating_nums': [4.6, 1.1, 6.45, 8.97]
    }

    for key, value in super_dict.items():
        print(key,'-',value)

    for value in super_list:
        print(value)


if __name__ == '__main__':
    main()