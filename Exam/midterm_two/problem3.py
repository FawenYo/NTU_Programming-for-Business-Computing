class Solution:
    def __init__(self):
        self.data = []
        self.action = ""
        self.columns = 0

    def main(self):
        file_path = input()
        self.action = input()
        # Read File
        with open(file_path, mode="r", encoding="cp950") as file:
            content = file.read()
            for each in content.split("\n"):
                if each:
                    data = each.split(",")
                    self.columns = len(data)
                    self.data.append(data)
        self.solution()

    def solution(self):
        if self.action == "TYPE":
            self.column_type()

        elif self.action == "MAXLEN":
            self.column_maxlen()

        elif self.action == "MAXNUMLEN":
            self.column_maxnumlen()

        elif self.action == "MAXDECPLACE":
            self.column_maxdecplace()

    def column_type(self):
        category = [0] * self.columns
        for each_row in self.data:
            for index, value in enumerate(each_row):
                try:
                    float(value)
                except ValueError:
                    category[index] = 1
        for index, each in enumerate(category):
            if each == 0:
                print("{}: {}".format(index, "numerical"))
            else:
                print("{}: {}".format(index, "categorical"))

    def column_maxlen(self):
        best = [0] * self.columns
        for each_row in self.data:
            for index, value in enumerate(each_row):
                value = value.strip(" ")
                if len(value) > best[index]:
                    best[index] = len(value)
        for i, v in enumerate(best):
            print("{}: {}".format(i, v))

    def column_maxnumlen(self):
        best = [0] * self.columns
        for each_row in self.data:
            for index, value in enumerate(each_row):
                try:
                    value = abs(float(value))
                    before_num = int(value)
                    if len(str(before_num)) > best[index]:
                        best[index] = len(str(before_num))
                # categorical
                except ValueError:
                    best[index] = 0
        for i, v in enumerate(best):
            print("{}: {}".format(i, v))

    def column_maxdecplace(self):
        best = [0] * self.columns
        for each_row in self.data:
            for index, value in enumerate(each_row):
                try:
                    float(value)
                    if "." in value:
                        digit = abs(float(value))
                        num_len = len(str(digit)) - len(str(int(digit))) - 1
                    # int 型態
                    else:
                        num_len = 0
                    if num_len > best[index]:
                        best[index] = num_len
                except ValueError:
                    best[index] = 0
        for i, v in enumerate(best):
            print("{}: {}".format(i, v))


if __name__ == "__main__":
    Solution().main()
