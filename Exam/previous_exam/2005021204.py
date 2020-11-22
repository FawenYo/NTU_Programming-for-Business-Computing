class Solution:
    def __init__(self):
        self.word_1 = ""
        self.operation = ""
        self.word_2 = ""

    def main(self):
        self.word_1, self.operation, self.word_2 = input().split(" ")
        self.calculate()

    def calculate(self):
        num_1 = self.word_to_num(text=self.word_1)
        num_2 = self.word_to_num(text=self.word_2)
        if self.operation == "plus":
            print(num_1 + num_2)
        else:
            print(num_1 - num_2)

    def word_to_num(self, text, num=0):
        # init
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        # calculate ten
        for index, value in enumerate(tens):
            if value in text:
                num += (index + 2) * 10
                text = text.replace(value, "")
        # calculate unit
        temp = 0
        for index, value in enumerate(units):
            if value in text:
                temp = index
        num += temp

        return num


if __name__ == '__main__':
    Solution().main()