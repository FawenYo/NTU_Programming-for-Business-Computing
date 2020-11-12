def main():
    user_input = input().split("'")
    text = user_input[1]
    offset = user_input[2][2:-1]
    answer = caesar(str_=text, n=offset)
    print(answer)


def caesar(str_, n):
    result = ""
    for each in str_:
        result += chr(ord(each) + int(n))
    return result


if __name__ == "__main__":
    main()
