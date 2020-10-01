import math


def main():
    input_list = []
    # 單位進貨成本, 單位零售價格, 需求的可能個數
    for index in range(3):
        user_input = input()
        input_list.append(int(user_input))
    # Probability list
    prob_demand = input_list[2]
    # +1 為 0銷售情況
    for index in range(prob_demand + 1):
        user_input = input()
        input_list.append(float(user_input))
    demand, max_profit = profit(input_list=input_list)
    print(demand, max_profit)


def profit(input_list):
    max_profit = 0
    # 單位進貨成本
    unit_input_price = input_list[0]
    # 單位零售價格
    unit_retail_price = input_list[1]
    # 需求的可能個數
    prob_demand = input_list[2]
    total_prob_list = input_list[3 : prob_demand + 4]
    for demand, each_probability in enumerate(total_prob_list):
        probability_list = input_list[3 : demand + 4]
        expected_profit = calculate_profit(
            unit_input_price=unit_input_price,
            unit_retail_price=unit_retail_price,
            probability_list=probability_list,
        )
        # 已達最大值 且 非 0
        if expected_profit <= max_profit and demand != 0:
            # 返回上一筆紀錄
            return demand - 1, max_profit
        else:
            max_profit = expected_profit
    return len(total_prob_list) - 1, max_profit


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
