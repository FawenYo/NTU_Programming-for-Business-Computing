# 城鎮數量
TOWN_NUMBER = 0
# 基地台數量
BASE_STATION = 0
# 訊號距離
DISTANCE = 0
# 城鎮座標
TOWN_COORDINATE = []
# 城鎮人口
TOWN_POPULATION = []


def main():
    global TOWN_NUMBER, BASE_STATION, DISTANCE
    # 城鎮數量 基地台數量 訊號距離
    TOWN_NUMBER, BASE_STATION, DISTANCE = [
        int(each_input) for each_input in input().split(" ")
    ]

    for each in range(TOWN_NUMBER):
        # x座標 y座標 人口數
        x_coordinate, y_coordinate, population = [
            int(each_input) for each_input in input().split(" ")
        ]
        TOWN_COORDINATE.append([x_coordinate, y_coordinate])
        TOWN_POPULATION.append(population)

    total_cover_population = 0
    chosen_location = []
    left_location = [i for i in range(TOWN_NUMBER)]

    for num in range(BASE_STATION):
        # 最佳選址位置, 覆蓋總人口, 剩餘地點
        location, cover_population, left_location = choose_location(
            left_location=left_location
        )
        total_cover_population += cover_population
        chosen_location.append(location)
    print(" ".join(str(i + 1) for i in chosen_location), str(total_cover_population))


def choose_location(left_location):
    best_town = 0
    best_population = 0
    best_nearby = []
    for index_i in left_location:
        value_i = TOWN_COORDINATE[index_i]
        station_cover_population = 0
        nearby_town = []

        for index_j in left_location:
            value_j = TOWN_COORDINATE[index_j]

            # 計算兩城鎮距離
            town_distance = distance_between(town_a=value_i, town_b=value_j)
            # 在訊號範圍之內
            if town_distance <= DISTANCE:
                nearby_town.append(index_j)
                station_cover_population += TOWN_POPULATION[index_j]
        # TODO: Performance Improve
        # 是否為最佳位置
        if station_cover_population > best_population:
            best_population = station_cover_population
            best_town = index_i
            best_nearby = nearby_town

    left_location = [i for i in left_location if i not in best_nearby]
    return best_town, best_population, left_location


# 計算兩城鎮距離
def distance_between(town_a, town_b):
    town_a_x, town_a_y = town_a
    town_b_x, town_b_y = town_b

    x_distance = town_a_x - town_b_x
    y_distance = town_a_y - town_b_y
    distance = (x_distance ** 2 + y_distance ** 2) ** (1 / 2)
    return distance


if __name__ == "__main__":
    main()
