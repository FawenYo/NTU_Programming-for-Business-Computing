import math


class Solution:
    def __init__(self):
        self.vectors = []

    def main(self):
        vector_num, dimension = [int(i) for i in input().split(",")]
        for each in range(vector_num):
            data = [int(i) for i in input().split(",")]
            self.vectors.append(data)
        self.solution()

    def solution(self):
        all_distance = []
        for index_i, value_i in enumerate(self.vectors):
            for index_j, value_j in enumerate(self.vectors[index_i + 1 :]):
                distance = self.calculate_distance(dim_1=value_i, dim_2=value_j)
                all_distance.append(distance)
        print(min(all_distance))

    def calculate_distance(self, dim_1, dim_2):
        distance = 0
        for index, value in enumerate(dim_1):
            temp = math.pow(value - dim_2[index], 2)
            distance += temp
        return int(distance)


if __name__ == "__main__":
    Solution().main()
