if __name__ == '__main__':
    mystr = input("Enter a line: ")
    words = mystr.split()
    wordList = []
    for word in words:
        wordList.append((len(word),word))
    sortedList = []
    wordList.sort()
    for length, word in wordList:
        sortedList.append(word)
    print(sortedList)
