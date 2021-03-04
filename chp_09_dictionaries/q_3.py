if __name__ == '__main__':
    fhand = open("demo.txt")
    messageCount = {}
    for line in fhand:
        if line.startswith('From'):
            words = line.split()
            messageCount[words[1]] = messageCount.get(words[1],0)+1

    valueList = list(messageCount.values())
    keyList = list(messageCount.keys())
    position = valueList.index(max(valueList))
    personWithMaxMails = keyList[position]
    print(personWithMaxMails + "With Mails " + str(max(valueList)))