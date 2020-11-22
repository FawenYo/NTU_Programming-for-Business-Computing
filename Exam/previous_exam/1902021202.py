class Solution:
    def __init__(self):
        self.hw_weight = 0
        self.mt1_weight = 0
        self.mt2_weight = 0
        self.final_weight = 0
        self.students = []

    def main(self):
        # 學生數量, 考試權重
        student_num, weights = input().split(";")
        self.hw_weight, self.mt1_weight, self.mt2_weight, self.final_weight = [
            float(x) for x in weights.split(",")
        ]

        input_hint = [i.lower() for i in input().split(",")]

        for i in range(int(student_num)):
            temp_0, temp_1, temp_2, temp_3, temp_4 = [
                float(x) for x in input().split(",")
            ]
            data = {
                input_hint[0]: temp_0,
                input_hint[1]: temp_1,
                input_hint[2]: temp_2,
                input_hint[3]: temp_3,
                input_hint[4]: temp_4,
            }
            self.students.append(data)
        self.solution()

    def solution(self):
        best = {"id": 1, "score": 0}
        for each in self.students:
            mt_score = min(each["mt1"], each["mt2"]) * min(
                self.mt1_weight, self.mt2_weight
            ) + max(each["mt1"], each["mt2"]) * max(self.mt1_weight, self.mt2_weight)
            score = (
                each["hw"] * self.hw_weight + mt_score + each["f"] * self.final_weight
            )
            if score > best["score"]:
                best["id"] = each["id"]
                best["score"] = score
            elif score == best["score"] and each["id"] < best["id"]:
                best["id"] = each["id"]

        print("{},{}".format(int(best["id"]), int(best["score"] / 100)))


if __name__ == "__main__":
    Solution().main()
