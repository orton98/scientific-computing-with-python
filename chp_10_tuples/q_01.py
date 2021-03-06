#Exercise 1: Revise a previous program as follows: Read and parse the "From"
#lines and pull out the addresses from the line. Count the number of messages
#from each person using a dictionary.

if __name__ == '__main__':
    fhand = open('demo.txt')
    messages = dict()
    for line in fhand:
        if line.startswith("From"):
            words = line.split()
            mail = words[1]
            messages[mail] = messages.get(mail, 0) + 1
    messageCount = []
    for (mail, count) in messages.items():
        messageCount.append((count, mail))
    messageCount.sort(reverse=True)
    print(messageCount[0][1] + " " + str(messageCount[0][0]))
