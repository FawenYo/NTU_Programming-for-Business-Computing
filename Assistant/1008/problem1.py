def main():
    input_list = input().split(",")
    for value in input_list[::2]:
        print(value)


if __name__ == '__main__':
    main()
