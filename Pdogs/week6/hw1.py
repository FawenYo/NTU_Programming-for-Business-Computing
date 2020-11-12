class HW1:
    def __init__(self):
        # 關鍵字
        self.keyword = ""
        # 字串
        self.string = ""

    def main(self):
        self.keyword = input()

        input_complete = False
        string_list = []
        while not input_complete:
            input_content = input()
            # 清除空白
            input_content.strip()
            if input_content != "INPUT_END":
                string_list.append(input_content)
            else:
                input_complete = True
        self.string = " ".join(string_list)

        answer = self.solution()
        print(answer)

    def solution(self):
        results = []
        index = self.string.find(self.keyword)
        while index != -1:
            before_text = self.string[index - 7 : index]
            # 關鍵字前不足7個字元
            if not before_text:
                before_text = self.string[:index]
            after_text = self.string[
                index + len(self.keyword) : index + len(self.keyword) + 7
            ]

            ans = "{}**{}**{}".format(
                before_text,
                self.keyword,
                after_text,
            )
            results.append(ans)
            # 更新 index 值
            index = self.string.find(self.keyword, index + len(self.keyword))
        if results:
            return "\n".join(results)
        else:
            return "NO_MATCH"


if __name__ == "__main__":
    HW1().main()
