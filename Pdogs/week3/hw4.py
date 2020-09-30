import math

# 商品價格
LEMON_PRICE = 7
ALMOND_OIL_PRICE = 0.6
HONEY_PRICE = 1.2
EGG_PRICE = 25


def main():
    # 睡眠時間天數
    sleep_days = int(input())

    sleep_times = []
    # 睡眠時數
    for i in range(sleep_days):
        sleep_times.append(float(input()))

    # math.floor => 無條件捨去
    print(math.floor(calculate(sleep_times=sleep_times)))


def calculate(sleep_times):
    # full_sleep: 睡眠時數 > 7 的 list
    full_sleep = list(value for value in sleep_times if value > 7)
    # 平均每日睡眠時間 = 全部睡眠時間加總 / 睡眠時間天數
    avg_sleep_time = sum(sleep_times) / len(sleep_times)

    lemon_face_mask = len(full_sleep)
    honey_face_mask = len(sleep_times) - lemon_face_mask if avg_sleep_time <= 6 else 0
    protein_face_mask = len(sleep_times) - lemon_face_mask if avg_sleep_time > 6 else 0

    return cost(
        lemon_face_mask=lemon_face_mask,
        honey_face_mask=honey_face_mask,
        protein_face_mask=protein_face_mask,
    )


# 計算成本
def cost(lemon_face_mask, honey_face_mask, protein_face_mask):
    global LEMON_PRICE

    # math.ceil => 無條件進位
    lemon = math.ceil(lemon_face_mask * 1.5)
    honey = math.ceil(honey_face_mask * 18 + protein_face_mask * 6)
    egg = math.ceil(protein_face_mask * 2)
    almond_oil = math.ceil(lemon_face_mask * 4 + honey_face_mask * 9)

    # 檸檬5顆以上打9折
    if lemon >= 5:
        LEMON_PRICE *= 0.9

    # 成本
    pay_cost = (
        lemon * LEMON_PRICE
        + honey * HONEY_PRICE
        + math.ceil(egg / 3) * EGG_PRICE
        + almond_oil * ALMOND_OIL_PRICE
    )
    return pay_cost


if __name__ == "__main__":
    main()
