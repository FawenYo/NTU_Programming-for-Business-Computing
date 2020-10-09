input_list = input().split(";")
result_list = []

for each in input_list:
    num = 0
    for character in each.split(","):
        num += ord(character) - 96
    result_list.append(num)
print(result_list)
