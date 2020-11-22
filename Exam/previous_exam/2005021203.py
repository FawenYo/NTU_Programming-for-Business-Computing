class Solution:
    def __init__(self):
        # 工作數
        self.jobs = 0
        # 尚未分配之員工
        self.remain_employee = []
        # 尚未分配之工作
        self.remain_jobs = []
        self.data = []
        # 分配結果
        self.result = []
        self.total_cost = 0

    def main(self):
        self.jobs = int(input())
        self.remain_employee = [int(i) for i in range(self.jobs)]
        self.remain_jobs = [int(i) for i in range(self.jobs)]
        self.result = [0 for i in range(self.jobs)]
        for i in range(self.jobs):
            temp = [int(i) for i in input().split(",")]
            self.data.append(temp)
        self.solution()

    def solution(self):
        for rounds in range(self.jobs):
            """ find min cost """
            data = {"min_cost": 999, "i": 0, "j": 0}
            for index_i, value_i in enumerate(self.data):
                for index_j, value_j in enumerate(value_i):
                    if (
                        index_i in self.remain_employee
                        and index_j in self.remain_jobs
                        and value_j < data["min_cost"]
                    ):
                        data["min_cost"] = value_j
                        data["i"] = index_i
                        data["j"] = index_j
            """ update data """
            self.remain_employee.remove(data["i"])
            self.remain_jobs.remove(data["j"])
            self.result[data["i"]] = data["j"]
            self.total_cost += data["min_cost"]

        print(
            "{};{}".format(",".join(str(i + 1) for i in self.result), self.total_cost)
        )


if __name__ == "__main__":
    Solution().main()
