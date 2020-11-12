class HW2:
    def __init__(self):
        self.width = 0
        self.keyword_one = ""
        self.keyword_two = ""
        self.string = ""

    def main(self):
        self.width = int(input())
        self.keyword_one = input()
        self.keyword_two = input()

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
        index_one = self.string.find(self.keyword_one)
        while index_one != -1:
            index_two = self.string.find(
                self.keyword_two, index_one + len(self.keyword_one)
            )
            while index_two != -1:
                # 兩關鍵詞間距
                width_between = index_two - index_one - len(self.keyword_one)
                # 關鍵字且間距離小於 width
                if index_two != -1 and width_between <= self.width:
                    # 關鍵字一前文字
                    before_text = self.string[index_one - 7 : index_one]
                    if not before_text:
                        before_text = self.string[:index_one]
                    # 兩關鍵字間文字
                    between_text = self.string[
                        index_one + len(self.keyword_one) : index_two
                    ]
                    # 關鍵字二後文字
                    after_text = self.string[
                        index_two
                        + len(self.keyword_two) : index_two
                        + len(self.keyword_two)
                        + 7
                    ]

                    ans = "{}**{}**{}**{}**{}".format(
                        before_text,
                        self.keyword_one,
                        between_text,
                        self.keyword_two,
                        after_text,
                    )
                    results.append(ans)
                index_two = self.string.find(
                    self.keyword_two, index_two + len(self.keyword_two)
                )
            index_one = self.string.find(
                self.keyword_one, index_one + len(self.keyword_one)
            )
        if results:
            return "\n".join(results)
        else:
            return "NO_MATCH"


if __name__ == "__main__":
    HW2().main()
