class HW3:
    def __init__(self):
        # 關鍵字
        self.keywords = []
        self.keywords_dict = {}
        # 新聞標題
        self.titles = []
        # 公司名稱
        self.companies = []
        # 個輪投資
        self.rounds = []
        # 剩餘投資股數
        self.remain_shares = 0

    def main(self):
        """ 資料輸入 """
        title_path = input()
        keyword_path = input()
        company_path = input()
        target, remain_shares, rounds_shares = input().split(",")
        self.remain_shares = int(remain_shares)
        for each in rounds_shares.split(":"):
            self.rounds.append(int(each))

        # 新聞標題
        with open(file=title_path, mode="r", encoding="utf-8") as file:
            raw_data = [i for i in file.read().split("\n") if i]
            for each in raw_data:
                self.titles.append(each.replace(" ", ""))

        # 關鍵字列表
        with open(file=keyword_path, mode="r", encoding="utf-8") as file:
            raw_data = [i for i in file.read().split("\n") if i]
            for each in raw_data:
                keyword, weight = each.split(" ")
                self.keywords_dict[keyword] = int(weight)
        # 關鍵字排序
        self.keyword_sort(keywords=list(self.keywords_dict.keys()))

        # 公司列表
        with open(file=company_path, mode="r", encoding="utf-8") as file:
            raw_data = [i for i in file.read().split("\n") if i]
            for each in raw_data:
                company, category = each.split(" ")
                if category == target:
                    self.companies.append(company)

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
        no_result = True
        result_companies = {}

        for title in self.titles:
            # (標題內是否包含公司, 公司名稱)
            companies = self.find_company(title=title)
            if companies:
                score = self.title_score(title=title)
                for company in companies:
                    if company in result_companies:
                        result_companies[company] += score
                    else:
                        result_companies[company] = score
                no_result = False

        if no_result:
            print("NO_MATCH")
        else:
            target_buy = self.calculate_shares(companies_data=result_companies)
            for company, shares in target_buy:
                if shares != 0:
                    print("{}購買{}張".format(company, shares))

    def find_company(self, title):
        """ 檢查標題內是否包含公司 """
        companies = []
        for company in self.companies:
            count = title.count(company)
            if count:
                # (公司名稱, 出現次數)
                companies.append(company)
        return companies

    def title_score(self, title):
        """ 計算標題分數 """
        score = 0
        # 優先切較長的關鍵字
        for keywords in self.keywords:
            # 偏移量
            offset = 0
            # 遍歷標題
            for chr_index in range(len(title)):
                # 關鍵字長度
                keywords_length = len(keywords[0])
                content = title[
                    chr_index + offset : chr_index + offset + keywords_length
                ]
                # 內容為關鍵字
                if content in keywords:
                    score += self.keywords_dict[content]
                    # 將關機字轉成 "|" 保護住
                    title = (
                        title[: chr_index + offset]
                        + "/"
                        + "|" * keywords_length
                        + "/"
                        + title[chr_index + offset + keywords_length :]
                    )
                    offset += 2
        return score

    def calculate_shares(self, companies_data):
        """ 計算個別公司投資股數 """
        sort_result = sorted(
            companies_data.items(), key=lambda x: (x[1], x[0]), reverse=True
        )[: len(self.rounds)]
        result = [[company, 0] for company, score in sort_result]
        while self.remain_shares > 0:
            for index, (company, score) in enumerate(sort_result):
                round_shares = self.rounds[index]

                if round_shares <= self.remain_shares:
                    result[index][1] += round_shares
                    self.remain_shares -= round_shares
                # 剩餘股數不足額
                else:
                    result[index][1] += self.remain_shares
                    self.remain_shares = 0
        return result


if __name__ == "__main__":
    HW3().main()
