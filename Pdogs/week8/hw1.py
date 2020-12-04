class Card:
    def __init__(self, suit, rank):
        self.suit = suit.split(",")
        self.rank = []
        self.rank_dictionary(raw_rank=rank)
        self.count_dict = {}
        self.count_rank()

    def rank_dictionary(self, raw_rank):
        raw_rank = raw_rank.split(",")
        rank_dict = {
            "A": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
        }
        for each in raw_rank:
            self.rank.append(rank_dict[each])
        self.rank.sort()

    def count_rank(self):
        for each in self.rank:
            if each in self.count_dict:
                self.count_dict[each] += 1
            else:
                self.count_dict[each] = 1

    def calculate(self):
        scores = [
            self.separate(),
            self.pairs(),
            self.flush(),
            self.straight(),
            self.full_house(),
            self.four_of_a_kind(),
            self.straight_flush(),
        ]
        print(max(scores))

    def separate(self):
        score = 0
        for each in self.rank:
            if each == 1:
                score += 1
        return score

    def pairs(self):
        """ 一對 """
        score = 0
        used = []
        sorted_rank = sorted(self.rank)
        for index, value in enumerate(sorted_rank[:-1]):
            if value == sorted_rank[index + 1] and value not in used:
                score += 2
                used.append(value)
        if 1 in self.count_dict and self.count_dict[1] == 1:
            return score + 1
        else:
            return score

    def flush(self):
        """ 同花 """
        if len(set(self.suit)) == 1:
            return 3
        else:
            return 0

    def straight(self):
        """ 順子 """
        exception = [
            [1, 10, 11, 12, 13],
            [1, 2, 11, 12, 13],
            [1, 2, 3, 12, 13],
            [1, 2, 3, 4, 13],
        ]

        # 點數中斷
        if self.rank in exception:
            return 5
        else:
            value_range = max(self.rank) - min(self.rank)
            if len(set(self.count_dict.values())) == 1 and (value_range == 4):
                return 5
            else:
                return 0

    def full_house(self):
        """ 葫蘆 """
        if sorted(self.count_dict.values()) == [2, 3]:
            return 10
        else:
            return 0

    def four_of_a_kind(self):
        """ 鐵支 """
        if sorted(self.count_dict.values()) == [1, 4]:
            if 1 in self.count_dict and self.count_dict[1] == 1:
                return 21
            else:
                return 20
        else:
            return 0

    def straight_flush(self):
        """ 同花順 """
        if self.flush() != 0 and self.straight() != 0:
            return 100
        else:
            return 0


if __name__ == "__main__":
    suit = input().replace(" ", "")
    rank = input().replace(" ", "")
    Card(suit=suit, rank=rank).calculate()
