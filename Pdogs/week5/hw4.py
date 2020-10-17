""" input data """
# 投資標的, 預算, 風險趨避
investment_targets, budget, risk_aversion = [int(i) for i in input().split(",")]
# 投資標的之資金需求
capital_needs = [int(i) for i in input().split(",")]
# 預期報酬
expected_returns = [int(i) for i in input().split(",")]
# 變異數
variances = []
for i in range(investment_targets):
    variances.append([int(i) for i in input().split(",")])

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
