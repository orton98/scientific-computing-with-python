if __name__ == '__main__':
    data = {
        'a' : 1,
        'b' : 10,
        'd' : 23,
        'g' : 5,
        'z' : 15
    }

    lst = []
    for key, value in data.items():
        # sort data dictionary by key
        lst.append((key, value))
        # sort data dictionary by value
        #lst.append((value, key))
    lst.sort()
    for l in lst:
        print(l[0])
        