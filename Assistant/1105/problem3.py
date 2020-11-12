def main():
    user_input = input()
    answer = solution(string=user_input)
    print(answer)


def solution(string):
    if string == string[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
