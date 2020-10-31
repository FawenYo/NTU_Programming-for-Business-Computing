""" 無條件捨去方法 """
# 1. math.floor => 這題不能用math QQ
# 2. int(n) => Python 預設直接砍掉浮點數部份
# 3. int(str(n).split('.')[0]) => 醜到不知道怎麼說ㄉ爛code :)

# 商品的種類數
PRODUCT_CATEGORY_AMOUNT = int(input())
# 組成套組的商品編號
PACK_PRODUCT_INDEX = []
for i in input().split(","):
    PACK_PRODUCT_INDEX.append(int(i))
# 商品價格
PRODUCT_PRICE_LIST = []
for i in input().split(","):
    PRODUCT_PRICE_LIST.append(int(i))
# 商品數量
PRODUCT_AMOUNT = []
for i in input().split(","):
    PRODUCT_AMOUNT.append(int(i))

""" Calculate Pack Amount """
arr = []
for i in PACK_PRODUCT_INDEX:
    arr.append(PRODUCT_AMOUNT[i - 1])

total_pack_amount = min(arr)
sale_pack_amount = total_pack_amount // 5
remain_pack_amount = total_pack_amount - sale_pack_amount * 5

""" Calculate Money """
pay_amount_sale = pay_amount_raw = 0
for index in range(PRODUCT_CATEGORY_AMOUNT):
    """ 原始價格 """
    pay_amount_raw += PRODUCT_AMOUNT[index] * PRODUCT_PRICE_LIST[index]

    """ 套組折扣 """
    product_index = index + 1
    if product_index in PACK_PRODUCT_INDEX:
        remain_product_amount = PRODUCT_AMOUNT[index] - total_pack_amount

        pay_amount_sale += (
            sale_pack_amount * 5 * 0.8
            + remain_pack_amount * 0.9
            + remain_product_amount
        ) * PRODUCT_PRICE_LIST[index]
    else:
        # 商品數量 * 商品價格
        pay_amount_sale += PRODUCT_AMOUNT[index] * PRODUCT_PRICE_LIST[index]

# 招募新人數量
recruitment = int((pay_amount_raw - pay_amount_sale) // 1000)

if recruitment > 0:
    print(str(int(pay_amount_sale)) + "," + str(recruitment))
else:
    print("So sad. I messed up.")
