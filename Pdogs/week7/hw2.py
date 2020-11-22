class HW2:
    def __init__(self):
        self.movie_data = {}
        self.genres_data = {}

    def main(self):
        item_path = input()
        genre_path = input()

        with open(file=genre_path, mode="r", encoding="ISO-8859-1") as file:
            raw_data = [i for i in file.read().split("\n") if i]
            for each in raw_data:
                category, index = each.split("|")
                self.genres_data[index] = category

        with open(file=item_path, mode="r", encoding="ISO-8859-1") as file:
            raw_data = [i for i in file.read().split("\n") if i]
            for each in raw_data:
                data = each.split("|")
                (
                    movie_id,
                    movie_title,
                    release_date,
                    video_release_date,
                    IMDb_URL,
                ) = data[:5]
                categories = []
                for index, genres in enumerate(data[5:]):
                    if genres == "1":
                        categories.append(self.genres_data[str(index)])
                temp = {
                    "movie_title": movie_title,
                    "release_date": release_date,
                    "video_release_date": video_release_date,
                    "IMDb_URL": IMDb_URL,
                    "categories": categories,
                }
                self.movie_data[movie_id] = temp
        target = input()
        self.solution(target=target)

    def solution(self, target):
        try:
            movie_result = self.movie_data[target]
            print(
                "{}: {}".format(
                    movie_result["movie_title"], ", ".join(movie_result["categories"])
                )
            )
        except KeyError:
            print("No movie found.")


if __name__ == "__main__":
    HW2().main()
