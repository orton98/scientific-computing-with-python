import string

if __name__ == '__main__':
    fhand = open('romeo.txt')
    wordCount = dict()
    for line in fhand:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            wordCount[word] = wordCount.get(word, 0)+1
    allWords = list()
    for word, count in wordCount.items():
        allWords.append((count, word))
    allWords.sort(reverse=True)
    print("Most Common Word: "+str(allWords[0][1]) + " With occurance of "+str(allWords[0][0]) + " times")