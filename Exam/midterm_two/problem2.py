class Solution:
    def __init__(self):
        self.titles = []
        self.punctuations = [",", ":", "."]

    def main(self):
        input_end = False
        while not input_end:
            title = input()
            if title != "INPUTSTOP":
                self.titles.append(title)
            else:
                input_end = True
        self.solution()

    def solution(self):
        for title in self.titles:
            # 去除頭尾的空白
            title = title.strip(" ")
            # 引號
            title = self.replace_quotes(title=title)
            # 連續空白
            while "  " in title:
                title = title.replace("  ", " ")
            # 標點符號
            title = self.clean_punctuation(title=title)
            print(title)

    def replace_quotes(self, title, temp=""):
        in_quotes = False
        for chr_index in range(len(title)):
            character = title[chr_index]

            if character != '"':
                temp += character
            else:
                # 引號不成對
                if '"' not in title[chr_index + 1 :] and not in_quotes:
                    temp += character
                else:
                    if not in_quotes:
                        in_quotes = True
                        temp += "「"
                    else:
                        in_quotes = False
                        temp += "」"
        return temp

    def clean_punctuation(self, title, temp=" "):
        for index in range(len(title)):
            character = title[index]

            if character not in self.punctuations:
                temp += character
            else:
                # 最後一個字
                if index + 1 == len(title):
                    # 前面不能有空白
                    if temp[-1] == " ":
                        temp = temp[:-1]
                    temp += character
                else:
                    # 前面不能有空白
                    if temp[-1] == " ":
                        temp = temp[:-1]
                    temp += character
                    # 後面要加空白
                    if title[index + 1] != " ":
                        temp += " "
        return temp.strip(" ")


if __name__ == "__main__":
    Solution().main()
