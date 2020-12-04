class Solution:
    def solution(self):
        frozen = Movie('Frozen', 2013, 'Jennifer', [1000, 200]) 
        lionKing = Movie('Lion King', 1994, 'Robert Ralph', [4000, 500])


        print(frozen.box_office()) # $1200 millions 
        print(frozen.is_earlier_than(lionKing)) # False


class Movie:
    def __init__(self, name, year, director, box):
        self.name = name
        self.year = year
        self.director = director
        self.box = box

    def box_office(self):
        result = 0
        for each in self.box:
            result += each
        return "${} millions".format(result)

    def is_earlier_than(self, other_movie):
        if self.year < other_movie.year:
            return True
        return False

if __name__ == "__main__":
    Solution().solution()