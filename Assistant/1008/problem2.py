input_list = input().split()
find_target = input()
find = False

for index, value in enumerate(input_list):
    if value == find_target:
        find = True
        print("Match", str(index))

if not find:
    print("None")