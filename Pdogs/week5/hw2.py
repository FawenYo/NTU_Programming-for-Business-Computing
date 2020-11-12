import math


def main():
    input_complete = False
    line_list = []
    while not input_complete:
        user_input = input()
        if user_input != "LINESTOP":
            line = [float(i) for i in user_input.split(",")]
            line_list.append(line)
        else:
            input_complete = True
    degree = float(input())
    answer = rotate(line_list=line_list, degree=degree)
    print(answer)


def rotate(line_list, degree=90):
    degree = math.pi / 180 * degree
    result = []
    temp = 0
    for line_index, line_value in enumerate(line_list):
        for index, value in enumerate(line_value):
            if index % 2 == 0:
                # NOTE: list is mutable, so we choose temp variable to remember last value.
                temp = line_value[index]
                line_value[index] = line_value[index] * math.cos(degree) + line_value[
                    index + 1
                ] * -math.sin(degree)
            else:
                line_value[index] = temp * math.sin(degree) + line_value[
                    index
                ] * math.cos(degree)
        result.append(
            "Line%d: %0.3f %0.3f %0.3f %0.3f"
            % (line_index, line_value[0], line_value[1], line_value[2], line_value[3])
        )
    return "\n".join(str(i) for i in result)


if __name__ == "__main__":
    main()
