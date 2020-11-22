from datetime import datetime


class Solution:
    def __init__(self):
        self.result = [0, 0, 0, 0, 0, 0, 0]

    def main(self):
        try:
            while True:
                user_input = input()
                if user_input != "BREAK":
                    self.find_date(user_input=user_input)
                else:
                    break
            for index, count in enumerate(self.result):
                print("{} {}".format(index + 1, count))
        except ValueError:
            print("DATA_ERROR")

    def find_date(self, user_input):
        year, month, day = [int(i) for i in user_input.split("/")]
        parse_date = datetime(year, month, day)
        # weekday from 0 to 6
        week_day = parse_date.weekday()
        self.result[week_day] += 1


if __name__ == "__main__":
    Solution().main()
