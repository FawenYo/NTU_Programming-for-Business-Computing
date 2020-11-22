def main():
    with open(file="lyrics.txt", mode="r", encoding="utf-8") as file:
        lyrics = file.read()
    answer = revert_song(lyrics=lyrics)
    print(answer)


def revert_song(lyrics):
    lyrics_list = [i for i in lyrics.split("\n") if i]
    answer = [""] * len(lyrics_list)
    for each in lyrics_list:
        num, lyric = each.split("@")
        answer[int(num)] = lyric
    return "\n".join(answer)


if __name__ == "__main__":
    main()
