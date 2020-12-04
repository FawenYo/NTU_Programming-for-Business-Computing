from datetime import datetime


class Solution:
    def __init__(self):
        self.current_date = datetime
        self.task = []
        self.input_contents = []
        self.dogs = {}

    def main(self):
        # 今天的日期
        self.current_date = datetime.strptime(input().replace(" ", ""), "%Y/%m/%d")
        # 指定的任務類別
        self.task = input().replace(" ", "").split(",")

        input_end = False
        while not input_end:
            input_content = input().replace(" ", "")
            if input_content != "Done":
                self.input_contents.append(input_content)
            else:
                input_end = True

        self.solution()

    def solution(self):
        # 事件
        self.process()

        task_event = self.task[0][4]
        if task_event == "A":
            """ 找出名字為給定名稱的狗狗 """
            name = self.task[1]
            dog = self.dogs[name]
            print("{},{},{},{}".format(dog.name, dog.height, dog.weight, dog.dust))
        elif task_event == "B":
            """ 找出散步頻率最低的狗 """
            # [(頻率, Dog's Object),]
            result = []
            for each in self.dogs:
                dog = self.dogs[each]
                walk_count = dog.walk_count
                duration = (self.current_date - dog.adopted_date).days
                frequency = walk_count / duration
                result.append((frequency, dog))
            # 散步頻率低 > 大型狗 > 體重重 > 身高高 > 名字長
            sorted_result = sorted(
                result,
                key=lambda e: (
                    e[0],
                    e[1].is_small_dog,
                    -e[1].weight,
                    -e[1].height,
                    -len(e[1].name),
                ),
            )
            dog = sorted_result[0][1]
            print("{},{},{},{}".format(dog.name, dog.height, dog.weight, dog.dust))
        elif task_event == "C":
            """ 找出最大散步間隔時間最長的狗狗 """
            # 間隔長 > 大型狗 > 體重重 > 身高高 > 名字長
            sorted_result = sorted(
                self.dogs.values(),
                key=lambda e: (
                    -e.max_interval,
                    e.is_small_dog,
                    -e.weight,
                    -e.height,
                    -len(e.name),
                ),
            )
            dog = sorted_result[0]
            print("{},{},{},{}".format(dog.name, dog.height, dog.weight, dog.dust))
        else:
            """ 找出累積灰塵量最多的狗狗 """
            # 灰塵多 > 大型狗 > 體重重 > 身高高 > 名字長
            sorted_result = sorted(
                self.dogs.values(),
                key=lambda e: (
                    -e.dust,
                    e.is_small_dog,
                    -e.weight,
                    -e.height,
                    -len(e.name),
                ),
            )
            dog = sorted_result[0]
            print("{},{},{},{}".format(dog.name, dog.height, dog.weight, dog.dust))

    def process(self):
        for input_content in self.input_contents:
            content = input_content.split("|")
            event = content[0]
            # 領養
            if event == "A":
                name, height, weight, adopted_date = content[1:]
                self.dogs[name] = Dog(
                    name=name, height=height, weight=weight, adopted_date=adopted_date
                )
            # 洗澡
            elif event == "B":
                name = content[1]
                self.dogs[name].bathe()
            # 散步
            elif event == "W":
                name, walk_date = content[1:]
                self.dogs[name].walk(walk_date=walk_date)
            # 換主人
            else:
                name = content[1]
                del self.dogs[name]


class Dog:
    def __init__(self, name, height, weight, adopted_date):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)
        self.adopted_date = datetime.strptime(adopted_date, "%Y/%m/%d")
        self.dust = 0
        self.walk_count = 0
        self.longest_duration = 0
        self.last_walk_date = datetime.strptime(adopted_date, "%Y/%m/%d")
        self.is_small_dog = self.check_if_small_dog()
        self.max_interval = 0

    def check_if_small_dog(self):
        """ 檢查是否為小型犬 """
        # 身高超過60 或 體重超過30
        if self.height > 60 or self.weight > 30:
            return False
        return True

    def walk(self, walk_date):
        """ 散步 """
        self.walk_count += 1
        # 更新最大間隔 & 最後一次散步日期
        walk_date = datetime.strptime(walk_date, "%Y/%m/%d")
        duration = (walk_date - self.last_walk_date).days
        if duration > self.max_interval:
            self.max_interval = duration
        self.last_walk_date = walk_date

        # 更新灰塵量
        if self.is_small_dog:
            self.dust += 3
        else:
            self.dust += 2

    def bathe(self):
        """ 洗澡 """
        self.dust = 0


if __name__ == "__main__":
    Solution().main()
