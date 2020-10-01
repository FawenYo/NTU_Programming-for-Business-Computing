import math

# 單位進貨成本
UNIT_INPUT_PRICE = 0
# 單位零售價格
UNIT_RETAIL_PRICE = 0
# 需求的可能個數
PROBABILITY_DEMAND = 0
# 單位殘值
UNIT_SALVAGE_VALUE = 0


def main():
    global UNIT_INPUT_PRICE, UNIT_RETAIL_PRICE, PROBABILITY_DEMAND, UNIT_SALVAGE_VALUE
    var_list = []
    input_list = []

    # 單位進貨成本, 單位零售價格, 需求的可能個數, 單位殘值
    for index in range(4):
        user_input = input()
        var_list.append(int(user_input))
    (
        UNIT_INPUT_PRICE,
        UNIT_RETAIL_PRICE,
        PROBABILITY_DEMAND,
        UNIT_SALVAGE_VALUE,
    ) = var_list

    # +1 為 0銷售情況
    for index in range(PROBABILITY_DEMAND + 1):
        user_input = input()
        input_list.append(float(user_input))
    demand, max_profit = profit(input_list=input_list)
    print(demand, max_profit)


def profit(input_list):
    result_list = []
    for demand, each_probability in enumerate(input_list):
        probability_list = input_list[: demand + 1]
        expected_profit = calculate_profit(probability_list=probability_list)
        result_list.append(expected_profit)
    max_value = max(result_list)
    return result_list.index(max_value), math.floor(max_value)


def calculate_profit(probability_list):
    final_profit = 0
    left_probability = 1
    # probability_list 包含 0銷售
    total_amount = len(probability_list) - 1
    for sale_amount, probability in enumerate(probability_list):
        # 利潤 = 單位零售價格 * 銷售個數
        revenue = UNIT_RETAIL_PRICE * sale_amount
        # 成本 = 單位進貨成本 * 總進貨數
        cost = UNIT_INPUT_PRICE * total_amount
        # 殘值 = 單位殘值 * 剩餘個數
        salvage_value = UNIT_SALVAGE_VALUE * (total_amount - sale_amount)
        # 收益 =  利潤 - 成本
        sale_profit = revenue - cost + salvage_value

        if sale_amount != total_amount:
            left_probability -= probability
        else:
            probability = left_probability
        final_profit += probability * sale_profit
    return final_profit


if __name__ == "__main__":
    main()
