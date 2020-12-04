class Solution:
    def __init__(self):
        self.user_input = ""
        self.number_dictionary = {
            "0": "零",
            "1": "一",
            "2": "二",
            "3": "三",
            "4": "四",
            "5": "五",
            "6": "六",
            "7": "七",
            "8": "八",
            "9": "九",
        }
        self.operations = {"+": "加", "-": "減", "*": "乘以", "/": "除以", "=": "等於"}

    def main(self):
        self.user_input = input()
        self.solution()

    def solution(self):
        result = ""
        for chr_index in range(len(self.user_input)):
            character = self.user_input[chr_index]

            if character in self.number_dictionary:
                # 非最後一個字元
                if chr_index + 1 != len(self.user_input):
                    next_character = self.user_input[chr_index + 1]
                    if next_character in self.number_dictionary:
                        result += self.number_dictionary[character] + "十"
                    else:
                        result += self.number_dictionary[character]
                else:
                    result += self.number_dictionary[character]
            else:
                result += self.operations[character]
        result = result.replace("一十", "十")
        result = result.replace("十零", "十")
        print(result)


if __name__ == "__main__":
    Solution().main()
