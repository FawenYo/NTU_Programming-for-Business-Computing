# Init variable
result = 0

user_input = int(input())
for value in range(1, user_input + 1):
    value_init = 1
    for each in range(1, value + 1):
        value_init *= each
    result += value_init
print(result)
