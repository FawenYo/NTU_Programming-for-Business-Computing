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
    x_offset, y_offset = [float(i) for i in input().split(",")]
    answer = plotshift(line_list=line_list, x_offset=x_offset, y_offset=y_offset)
    print(answer)


def plotshift(line_list, x_offset=0, y_offset=0):
    result = []
    for line_index, line_value in enumerate(line_list):
        for index, value in enumerate(line_value):
            if index % 2 == 0:
                line_value[index] = value + x_offset
            else:
                line_value[index] = value + y_offset
        result.append(
            "Line%d: %0.3f %0.3f %0.3f %0.3f"
            % (line_index, line_value[0], line_value[1], line_value[2], line_value[3])
        )
    return "\n".join(str(i) for i in result)


if __name__ == "__main__":
    main()
