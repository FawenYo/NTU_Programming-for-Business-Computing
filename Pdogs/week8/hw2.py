class Solution:
    def __init__(self):
        self.scores = []

    def main(self):
        all_cards = Deck().main()
        for player_cards in all_cards:
            suits = []
            ranks = []
            for card in player_cards:
                suits.append(card[0])
                ranks.append(int(card[1:]))
            score = Card(suit=suits, rank=ranks).calculate()
            self.scores.append(str(score))
        print(",".join(self.scores))


class Deck:
    def __init__(self):
        self.players = 0
        self.result = []
        self.cards = []

    def main(self):
        self.players = int(input())
        for i in range(self.players):
            self.cards.append(input().replace(" ", "").split(","))
        return self.add_card()

    def card_value(self, card):
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
        suit = card[0]
        rank = card[1:]
        return suit, rank_dict[rank]

    def add_card(self):
        for player in self.cards:
            player_cards = []
            for card in player:
                suit, rank = self.card_value(card=card)
                if len(player_cards) < 5:
                    # A的前一張為K
                    if rank == 1:
                        previous_card = "{}{}".format(suit, 13)
                    else:
                        previous_card = "{}{}".format(suit, int(rank) - 1)

                    if previous_card not in player_cards:
                        player_cards.append("{}{}".format(suit, rank))
                    else:
                        player_cards.remove(previous_card)
                else:
                    break
            self.result.append(player_cards)
        return self.result


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = sorted(rank)
        self.count_dict = {}
        self.count_rank()

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
        return max(scores)

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
        return score

    def flush(self):
        """ 同花 """
        if len(set(self.suit)) == 1 and len(self.rank) == 5:
            return 3
        return 0

    def straight(self):
        if len(self.rank) != 5:
            return 0
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
            return 0

    def full_house(self):
        """ 葫蘆 """
        if sorted(self.count_dict.values()) == [2, 3]:
            return 10
        return 0

    def four_of_a_kind(self):
        """ 鐵支 """
        if sorted(self.count_dict.values()) == [1, 4]:
            if 1 in self.count_dict and self.count_dict[1] == 1:
                return 21
            return 20
        return 0

    def straight_flush(self):
        """ 同花順 """
        if self.flush() != 0 and self.straight() != 0:
            return 100
        return 0


if __name__ == "__main__":
    Solution().main()
