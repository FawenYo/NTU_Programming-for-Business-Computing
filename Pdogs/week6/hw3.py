class HW3:
    def __init__(self):
        # 公司
        self.companies = []
        # 全部關鍵字
        self.keywords = []
        # 新聞標題
        self.titles = []

    def main(self):
        """ 資料輸入 """
        input_complete = False

        self.companies = input().split(",")
        keywords = input().split(",")
        # 優先切長度較長的關鍵字
        self.keyword_sort(keywords=keywords)

        while not input_complete:
            user_input = input()
            if user_input != "INPUT_END":
                self.titles.append(user_input.replace(" ", ""))
            else:
                input_complete = True
        self.solution()

    def keyword_sort(self, keywords):
        # key: 字串長度, value: 該長度的子list
        keyword_dict = {}
        for each in keywords:
            keyword_length = len(each)
            # 加進相同長度的list
            if keyword_length in keyword_dict:
                keyword_dict[keyword_length].append(each)
            else:
                keyword_dict[keyword_length] = [each]
        for value in keyword_dict.values():
            self.keywords.insert(0, value)

    def solution(self):
        for title in self.titles:
            # (標題內是否包含公司, 公司名稱)
            companies = self.find_company(title=title)
            if companies:
                result = self.title_split(title=title)
                answer = ",".join(str(i[0]) for i in companies) + ";" + result
                print(answer)
            else:
                print("NO_MATCH")

    def find_company(self, title):
        """ 檢查標題內是否包含公司 """
        companies = []
        for company in self.companies:
            count = title.count(company)
            if count:
                # (公司名稱, 出現次數)
                companies.append((company, count))
        companies.sort(key=lambda element: (-element[1]))
        return companies

    def title_split(self, title):
        temp = title
        # 優先切較長的關鍵字
        for keywords in self.keywords:
            # 偏移量
            offset = 0
            # 遍歷標題
            for chr_index in range(len(temp)):
                # 關鍵字長度
                keywords_length = len(keywords[0])
                content = temp[chr_index + offset: chr_index + offset + keywords_length]
                # 內容為關鍵字
                if content in keywords:
                    # 將關機字轉成 "|" 保護住
                    temp = temp[:chr_index + offset] + "/" + "|" * keywords_length + "/" + temp[chr_index + offset + keywords_length:]
                    offset += 2
        # 前後皆為關鍵字
        while "//" in temp:
            temp = temp.replace("//", "/")
        return self.revert_to_title(title=title, temp=temp)


    def revert_to_title(self, title, temp):
        i = 0
        answer = ""
        for each in temp:
            if each != "/":
                if each == "|":
                    answer += title[i]
                else:
                    answer += each
                i += 1
            else:
                answer += each
        return answer.strip("/")


if __name__ == "__main__":
    HW3().main()
