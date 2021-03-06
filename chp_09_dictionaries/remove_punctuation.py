import string

if __name__ == '__main__':
    count = dict()
    fhand = open('romeo.txt')
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            count[word] = count.get(word,0) + 1
    print(count)
