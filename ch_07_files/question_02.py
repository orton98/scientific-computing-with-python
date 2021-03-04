if __name__ == '__main__':
    try:
        fhand = open("demo.txt")
    except:
        print(" file not exists")
        quit()
    total_lines = 0
    sum = 0
    for l in fhand:
       if l.startswith("X-DSPAM-Confidence:"):
           total_lines+=1
           value = l.split(':')[-1]
           sum+=float(value)
    print(total_lines)
    print("average",str(sum/total_lines))