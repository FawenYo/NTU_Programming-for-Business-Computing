table_num = int(input())

# ver.1
for i in range(1, table_num + 1):
    for j in range(1, table_num + 1):
        print(i * j, end="    ")
    print("\n")

# ver.2
for i in range(1, table_num + 1):
    for j in range(1, table_num + 1):
        print(i, "*", j, "=", i * j, end="    ")
    print("\n")
