class Solution:
    def __init__(self):
        # 載客限制
        self.limit = 0
        # 上車人數
        self.ups = []
        # 下車人數
        self.downs = []
        # 載客量
        self.passengers = 0
        # 錯誤碼
        self.error_code = 0

    def main(self):
        # 車站數量, 乘客限制
        stations, self.limit = [int(i) for i in input().split(",")]
        # 下車
        self.downs = [int(i) for i in input().split(",")]
        # 上車
        self.ups = [int(i) for i in input().split(",")]

        self.solution()

    def solution(self):
        for each in zip(self.downs, self.ups):
            down, up = each

            # 乘客下車
            self.passengers -= down
            if self.error_code == 0 and self.passengers < 0:
                self.error_code = 1

            # 乘客上車
            self.passengers += up
            if self.error_code == 0 and self.passengers > self.limit:
                self.error_code = 2

        print("{},{}".format(self.passengers, self.error_code))


if __name__ == "__main__":
    Solution().main()
