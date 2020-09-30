loop_num = int(input())

for index in range(loop_num):
    value = index + 1
    if value != loop_num:
        print(value, end=",")
    else:
        print(value)
