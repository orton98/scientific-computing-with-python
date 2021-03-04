if __name__ == '__main__':
    fhand = open('words.txt')
    all_words = {}
    for line in fhand:
        words = line.split()
        if len(words) > 0:
            for word in words:
                all_words[word] = "abcd"
    my_word = input("Enter a word to find: ")
    if my_word in all_words:
        print("Found")
    else:
        print("Not found!")