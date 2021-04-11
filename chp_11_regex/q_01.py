import re

if __name__ == '__main__':
    fhand = open('contact.txt')
    userInput = input("Enter a regular expression: ")
    count = 0
    for line in fhand:
        line = line.rstrip()
        if re.search('$userInput', line):
            count += 1
    print(f"contact.txt had {count} lines that matched {userInput}")