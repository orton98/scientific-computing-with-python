import re
if __name__ == '__main__':
    fhand = open('contact.txt')
    for line in fhand:
        if re.search('From:',line):
            print(line)
