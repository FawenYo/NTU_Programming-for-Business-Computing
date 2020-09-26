# 初始赴約意願值
willing_init = 0.5

# PM2.5 濃度
pm_concentration = int(input())
# 氣溫
temperature = int(input())
# 露點溫度
dew_point_temperature = int(input())
# 赴約臨界值
critical_value = float(input())

# 空汙影響赴約意願值計算
if pm_concentration <= 35:
    willing_air_pollution = willing_init + (100 - pm_concentration) * 0.005
else:
    willing_air_pollution = willing_init + (45 - pm_concentration) * 0.02

# 相對溼度影響赴約意願值計算
humidity = 100 - 5 * (temperature - dew_point_temperature)
if humidity <= 30:
    willing_humidity = willing_init / 60 * (110 - humidity)
else:
    willing_humidity = willing_init / 45 * (90 - humidity)

# 調整value
if willing_air_pollution < 0:
    willing_air_pollution = 0
elif willing_air_pollution > 1:
    willing_air_pollution = 1

if willing_humidity < 0:
    willing_humidity = 0
elif willing_humidity > 1:
    willing_humidity = 1

# 取min值
if willing_air_pollution >= willing_humidity:
    determine_value = willing_humidity
else:
    determine_value = willing_air_pollution

# 赴約意願
if determine_value >= critical_value:
    determine = "Let's go together."
else:
    determine = "I wouldn't go out with you."

print("{:.2f}".format(determine_value))
print(determine)
