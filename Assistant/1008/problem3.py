input_list = input().split(",")
result_num = 0
result_list = []

for index in range(len(input_list)):
    result_num += int(input_list[index])
    result_list.append(result_num)
    print(",".join(str(i) for i in result_list))
