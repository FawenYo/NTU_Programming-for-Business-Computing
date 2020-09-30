def main():
    food_price = int(input())
    mood = int(input())
    weather = int(input())
    if food_price <= 100:
        print("Yes")
    else:
        if mood == 1 and weather == 1:
            food_price *= 0.5
        elif mood == 1 and weather == 0:
            food_price *= 0.7
        elif mood == 0 and weather == 1:
            food_price *= 0.9
        if food_price <= 100:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
