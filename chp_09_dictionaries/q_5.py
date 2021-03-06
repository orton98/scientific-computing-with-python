if __name__ == '__main__':
    fhand = open("../chp_10_tuples/demo.txt")
    domains = []
    for line in fhand:
        if line.startswith('From'):
            words = line.split()
            domain = words[1].split("@")
            domain = domain[1]
            domains.append(domain)
    print(domains)