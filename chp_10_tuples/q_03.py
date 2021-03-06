import string

# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all the input
# to lower case and only count the letters a-z. Your program should not count
# spaces, digits, punctuation, or anything other than the letters a-z.

if __name__ == '__main__':
    fhand = open('demo.txt')
    characterCount = dict()
    for line in fhand:
        line = line.lower()
        line = line.translate(line.maketrans('','',string.punctuation))
        words = line.split()
        for word in words:
            for character in word:
                if character.isalpha():
                    characterCount[character] = characterCount.get(character, 0) + 1
    charList = list()
    for (character, count) in characterCount.items():
        charList.append((count, character))
    charList.sort()
    for item in charList:
        print(item[1] + ": " + str(item[0]))