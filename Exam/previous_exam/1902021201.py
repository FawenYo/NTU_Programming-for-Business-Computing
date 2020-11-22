class Solution:
    def __init__(self):
        self.hw_weight = 0
        self.mt1_weight = 0
        self.mt2_weight = 0
        self.final_weight = 0
        self.students = []

    def main(self):
        student_num, weights = input().split(";")
        self.hw_weight, self.mt1_weight, self.mt2_weight, self.final_weight = [
            float(x) for x in weights.split(",")
        ]

        input_hint = input()

        for i in range(int(student_num)):
            id, hw, mt1, mt2, f = [float(x) for x in input().split(",")]
            data = {"id": id, "hw": hw, "mt1": mt1, "mt2": mt2, "f": f}
            self.students.append(data)
        self.solution()

    def solution(self):
        best = {"id": 1, "score": 0}
        for each in self.students:
            score = (
                each["hw"] * self.hw_weight
                + each["mt1"] * self.mt1_weight
                + each["mt2"] * self.mt2_weight
                + each["f"] * self.final_weight
            )
            if score > best["score"]:
                best["id"] = each["id"]
                best["score"] = score
            elif score == best["score"] and each["id"] < best["id"]:
                best["id"] = each["id"]

        print("{},{}".format(int(best["id"]), int(best["score"] / 100)))


if __name__ == "__main__":
    Solution().main()
