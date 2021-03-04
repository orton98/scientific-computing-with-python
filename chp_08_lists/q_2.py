# Write a program to read through the mail box data and when you find line
# that starts with "From", you will split the line into words using the
# split function. We are interested in who sent the message, which is the second
# word on the From line.


if __name__ == '__main__':
    try:
        fhand = open('demo.txt')
    except:
        print("file not found")
        quit()
    for l in fhand:
        if l.startswith("From"):
            words = l.split()
            if len(words) >0 :
                print(words[1])