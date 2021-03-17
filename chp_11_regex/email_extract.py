import re

if __name__ == '__main__':
    fhand = open('contact.txt')
    for line in fhand:
        lst = re.findall("[a-zA-z0-9]\S*@\S*[a-zA-z0-9]", line)
        if len(lst) > 0:
            print(lst)
