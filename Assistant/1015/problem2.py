def main():
    player_one = input().split(",")
    player_two = input().split(",")
    answer = solution(player_one=player_one, player_two=player_two)
    print(answer)


def solution(player_one, player_two):
    hit_one, hit_nums_one = calculate(data=player_one)
    hit_two, hit_nums_two = calculate(data=player_two)
    if hit_one * hit_nums_two > hit_two * hit_nums_one:
        return "1,{}".format(hit_one)
    elif hit_one * hit_nums_two < hit_two * hit_nums_one:
        return "2,{}".format(hit_two)
    else:
        if hit_one >= hit_two:
            return "1,{}".format(hit_one)
        elif hit_one < hit_two:
            return "2,{}".format(hit_two)


def calculate(data):
    # 安打
    hit = 0
    # 出局
    out = 0

    for each in data:
        if each == "o":
            hit += 1
        elif each == "x":
            out += 1

    # 打數
    hit_nums = hit + out

    return hit, hit_nums


if __name__ == "__main__":
    main()
