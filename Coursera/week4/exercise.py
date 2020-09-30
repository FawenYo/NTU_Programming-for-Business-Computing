import math


def main():
    input_list = []
    # N = 8, N+5 = 13
    # 單位進貨成本, 單位零售價格, 需求的可能個數, 訂貨量
    for index in range(4):
        user_input = input()
        input_list.append(int(user_input))
    # Probability list
    for index in range(9):
        user_input = input()
        input_list.append(float(user_input))
    print(profit(input_list=input_list))


def profit(input_list):
    # 單位進貨成本
    unit_input_price = input_list[0]
    # 單位零售價格
    unit_retail_price = input_list[1]
    # 需求的可能個數 = 8
    prob_demand = input_list[2]
    # 訂貨量
    demand = input_list[3]

    probability_list = input_list[4 : demand + 5]
    expected_profit = calculate_profit(
        unit_input_price=unit_input_price,
        unit_retail_price=unit_retail_price,
        probability_list=probability_list,
    )
    return expected_profit


def calculate_profit(unit_input_price, unit_retail_price, probability_list):
    final_profit = 0
    used_probability = []
    demand_amount = len(probability_list) - 1
    for sale_amount, probability in enumerate(probability_list):
        # 利潤 = 單位零售價格 * 銷售個數
        revenue = unit_retail_price * sale_amount
        # 成本 = 單位進貨成本 * 總進貨數
        cost = unit_input_price * demand_amount
        # 收益 =  利潤 - 成本
        sale_profit = revenue - cost

        if sale_amount != len(probability_list) - 1:
            weight = probability
            used_probability.append(probability)
        # 剩餘 probability 加總
        else:
            weight = 1
            for each_probability in used_probability:
                weight -= each_probability
        final_profit += weight * sale_profit
    return math.floor(final_profit)


if __name__ == "__main__":
    main()
