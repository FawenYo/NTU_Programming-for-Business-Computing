def main():
    lyrics = input()
    answer = count_word(lyrics=lyrics)
    print(answer)


def count_word(lyrics):
    word_dict = {}
    for word in lyrics:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


if __name__ == "__main__":
    main()
