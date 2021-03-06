# Exercise 2: This program counts the distribution of the hour of the day for
# each of the messages. You can pull the hour from the "From" line by finding
# the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts,
# one per line, sorted by hour as shown below.

if __name__ == '__main__':
    fhand = open('demo.txt')
    hourCount = dict()
    for line in fhand:
        if line.startswith('From'):
            words = line.split()
            if len(words) > 6:
                timeStr = words[5]
                hour = timeStr[0:2]
                hourCount[hour] = hourCount.get(hour, 0) + 1
    hourList = list()
    for (hour, count) in hourCount.items():
        hourList.append((hour, count))
    hourList.sort()
    for hour in hourList:
        print(str(hour[0]) + " " + str(hour[1]))
