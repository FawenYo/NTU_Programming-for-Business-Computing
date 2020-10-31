# x 座標上限
X_LIMIT = 0
# y 座標上限
Y_LIMIT = 0
# 覆蓋距離
COVER_DISTANCE = 0
# 座標點
POINTS = []


def main():
    global X_LIMIT, Y_LIMIT, COVER_DISTANCE, POINTS
    X_LIMIT, Y_LIMIT, COVER_DISTANCE = [int(i) for i in input().split(",")]
    for y_index in range(Y_LIMIT + 1):
        populations = [int(i) for i in input().split(",")]
        for x_index, value in enumerate(populations):
            point_data = [x_index, y_index, value]
            POINTS.append(point_data)
    answer = solution()
    print(answer)


def solution():
    result = 0
    for x_index in range(X_LIMIT + 1):
        for y_index in range(Y_LIMIT + 1):
            current_point = [x_index, y_index]
            cover_population = coverage(current_point=current_point)
            if cover_population >= result:
                result = cover_population
    return result


def coverage(current_point):
    cover_population = 0
    for each_point in POINTS:
        distance = calculate_distance(
            current_point=current_point, each_point=each_point
        )
        if distance <= COVER_DISTANCE:
            cover_population += each_point[2]
    return cover_population


def calculate_distance(current_point, each_point):
    current_point_x, current_point_y = current_point
    each_point_x, each_point_y = each_point[:-1]

    x_distance = current_point_x - each_point_x
    y_distance = current_point_y - each_point_y
    x_distance = x_distance if x_distance >= 0 else -x_distance
    y_distance = y_distance if y_distance >= 0 else -y_distance
    distance = x_distance + y_distance
    return distance


if __name__ == "__main__":
    main()
