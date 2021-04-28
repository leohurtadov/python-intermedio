def main():
    # my_list = []

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_list.append(i**2)
    
    # print(my_list)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)


if __name__ == '__main__':
    main()