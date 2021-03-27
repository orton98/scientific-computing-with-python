import re

if __name__ == '__main__':
    fhand = open('contact.txt')
    for line in fhand:
        line = line.rstrip()
        # x = re.findall("^X\S*: ([0-9.]+)", line)
        # x = re.findall('^Details:.*rev=([0-9.]+)', line)
        x = re.findall('^From .* ([0-9][0-9]):', line)
        if len(x) > 0:
            print(x)