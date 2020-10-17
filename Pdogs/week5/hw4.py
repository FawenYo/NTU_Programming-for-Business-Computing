""" input data """
input_data = input().split(",")
# 投資標的
investment_targets = int(input_data[0])
# 預算
budget = int(input_data[1])
# 風險趨避
risk_aversion = int(input_data[2])


# 投資標的之資金需求
capital_needs = []
for i in input().split(","):
    capital_needs.append(int(i))
# 預期報酬
expected_returns = []
for i in input().split(","):
    expected_returns.append(int(i))
# 變異數
variances = []
for i in range(investment_targets):
    insert_data = []
    for each_i in input().split(","):
        insert_data.append(int(each_i))
    variances.append(insert_data)

""" main() """
# result
result = []

for i in range(investment_targets):
    """ choose best """
    max_profit = 0
    current_best_index = 0
    for index in range(investment_targets):
        # 還沒選過且未超出剩餘預算
        if index not in result and capital_needs[index] <= budget:
            """ calculate profit """
            impact = 0
            for each_index in result:
                impact += 2 * variances[each_index][index]

            each_result = expected_returns[index] - risk_aversion * (
                    variances[index][index] + impact
            )

            """ update local max value """
            if each_result > max_profit:
                max_profit = each_result
                current_best_index = index
            elif each_result == max_profit and each_result != 0:
                if capital_needs[index] < capital_needs[current_best_index]:
                    current_best_index = index
    """ update global max value """
    if max_profit != 0:
        result.append(current_best_index)
        previous_index = current_best_index
        budget -= capital_needs[current_best_index]
    else:
        break

# sort result list
result.sort()
if result:
    answer = ""
    for index in range(len(result)):
        if index + 1 != len(result):
            answer += str(result[index] + 1) + ","
        else:
            answer += str(result[index] + 1)
    print(answer)
else:
    print("0")
