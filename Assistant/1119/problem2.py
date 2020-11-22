class Solution2:
    def __init__(self):
        self.user_input = []

    def main(self):
        self.user_input = input().split(" ")
        self.solution()

    def solution(self):
        word_dict = {}
        most_word = ""
        most_count = 0
        for each in self.user_input:
            each = each.lower()
            each = each.strip(",.:;!?")
            if each:
                if each in word_dict:
                    word_dict[each] += 1
                else:
                    word_dict[each] = 1
        for word, word_count in word_dict.items():
            if word_count > most_count:
                most_count = word_count
                most_word = word
            elif word_count == most_count and word < most_word:
                most_word = word
        print("{},{}".format(most_word, most_count))


if __name__ == "__main__":
    Solution2().main()