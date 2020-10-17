MERCHANTS = 0
PRODUCTS = 0
TRANSACTIONS = 0
TARGET_PRODUCT = 0


def main():
    global MERCHANTS, PRODUCTS, TRANSACTIONS, TARGET_PRODUCT
    MERCHANTS, PRODUCTS, TRANSACTIONS, TARGET_PRODUCT = [
        int(i) for i in input().split(",")
    ]

    input_list = []
    for i in range(TRANSACTIONS):
        input_data = [int(i) for i in input().split(",")]
        input_list.append(input_data)
    highest_score, merchants = solution(inputs=input_list)
    print("{}:".format(highest_score) + ",".join(merchants))


def solution(inputs):
    data = []
    for each in inputs:
        if each[1] == TARGET_PRODUCT:
            data.append(each)
    # [商人編號, 商品名稱, 評分]
    sorted_list = sorted(data, key=lambda tup: (-tup[2], tup[0], tup[1]))
    highest_score = sorted_list[0][2]
    merchants = [str(sorted_list[0][0])]
    for each in sorted_list[1:]:
        if each[2] == highest_score:
            merchants.append(str(each[0]))
        else:
            return highest_score, merchants
    return highest_score, merchants


if __name__ == "__main__":
    main()
