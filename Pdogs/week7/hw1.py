import operator


class HW1:
    def __init__(self):
        self.titles = []
        self.target = ""

    def main(self):
        file_path = input()
        self.target = input()
        # Read data from file
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            raw_data = file.read().split("\n")
            for each in raw_data:
                self.titles += each.split("\t")
        # remove last line
        if not self.titles[-1]:
            self.titles.pop()
        self.solution()

    def solution(self):
        before_result = self.find_before()
        print("熱門前一個字:")
        for each in before_result:
            word = each[0]
            print("{}---{}".format(word, self.target))
        after_result = self.find_after()
        print("熱門下一個字:")
        for each in after_result:
            word = each[0]
            print("{}---{}".format(self.target, word))

    def find_before(self):
        count_dict = {}
        for title in self.titles:
            title = title.strip(" \t\n")
            index = title.find(self.target)
            while index != -1:
                if index != 0:
                    before_word = title[index - 1]
                    if before_word in count_dict:
                        count_dict[before_word] += 1
                    else:
                        count_dict[before_word] = 1
                title = title[:index] + "|" + title[index + 1 :]
                index = title.find(self.target)
        temp = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)
        result = sorted(temp, key=lambda x: (x[1], ord(x[0])), reverse=True)
        return result[:10]

    def find_after(self):
        count_dict = {}
        for title in self.titles:
            title = title.strip(" \t\n")
            index = title.find(self.target)
            while index != -1:
                try:
                    after_word = title[index + len(self.target)]
                    if after_word in count_dict:
                        count_dict[after_word] += 1
                    else:
                        count_dict[after_word] = 1
                except:
                    pass
                title = title[:index] + "|" + title[index + 1 :]
                index = title.find(self.target)
        temp = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)
        result = sorted(temp, key=lambda x: (x[1], ord(x[0])), reverse=True)
        return result[:10]


if __name__ == "__main__":
    HW1().main()
