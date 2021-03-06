if __name__ == '__main__':
    fhand = open('../chp_10_tuples/demo.txt')
    days = {}
    for line in fhand:
        if line.startswith('From'):
            words = line.split()
            if len(words) > 3:
                days[words[2]] = days.get(words[2],0) +1
    print(days)