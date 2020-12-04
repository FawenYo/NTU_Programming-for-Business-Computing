class Solution:
    def __init__(self):
        self.lines = []
        self.horv = ""
        self.loc = 0.0

    def main(self):
        input_end = False
        while not input_end:
            user_input = input()
            if user_input != "LINESTOP":
                data = [float(i) for i in user_input.split(",")]
                self.lines.append(data)
            else:
                input_end = True
        self.horv, loc = input().split(",")
        self.loc = float(loc)

        self.plotmirror()

    def plotmirror(self):
        # 垂直鏡射
        if self.horv == "v":
            for index, each_line in enumerate(self.lines):
                new_x1 = self.mirror_loc(loc=each_line[0])
                y1 = each_line[1]
                new_x2 = self.mirror_loc(loc=each_line[2])
                y2 = each_line[3]
                print(
                    "Line%d: %0.3f %0.3f %0.3f %0.3f" % (index, new_x1, y1, new_x2, y2)
                )
        # 水平鏡射
        else:
            for index, each_line in enumerate(self.lines):
                x1 = each_line[0]
                new_y1 = self.mirror_loc(loc=each_line[1])
                x2 = each_line[2]
                new_y2 = self.mirror_loc(loc=each_line[3])
                print(
                    "Line%d: %0.3f %0.3f %0.3f %0.3f" % (index, x1, new_y1, x2, new_y2)
                )

    def mirror_loc(self, loc):
        if loc < self.loc:
            return loc + (self.loc - loc) * 2
        else:
            return loc - (loc - self.loc) * 2


if __name__ == "__main__":
    Solution().main()
