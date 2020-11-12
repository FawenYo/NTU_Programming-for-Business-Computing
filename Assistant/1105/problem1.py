def main():
    user_input = input()
    count, character = countCharacter(str_=user_input)
    print(str(count) + "," + str(character))


def countCharacter(str_):
    string_list = []
    count_list = []
    for each in str_:
        try:
            index = string_list.index(each)
            count_list[index] += 1
        except ValueError:
            string_list.append(each)
            count_list.append(1)
    max_index = count_list.index(max(count_list))
    return string_list[max_index], count_list[max_index]


if __name__ == "__main__":
    main()
