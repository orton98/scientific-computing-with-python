if __name__ == '__main__':
    fname = input("enter file name")
    if "na na boo boo" in fname:
        print("You have been punked!")
        quit()
    try:
        fhand = open(fname)
    except:
        print(fname + " file does not exists")
        quit()
    fr = fhand.read()
    print(len(fr))