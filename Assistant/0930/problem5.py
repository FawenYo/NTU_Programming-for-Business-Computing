for i in range(1, 101):
    if i % 3 == 0 or i % 10 == 3 or i // 10 == 3:
        continue
    print(i, end=" ")
