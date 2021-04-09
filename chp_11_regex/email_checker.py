import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check(e):
    if re.search(regex, e):
        data = e.split('@')
        print("email: ", e, " , username: ", data[0], " , host: ", data[1])
    else:
        print("Not a valid email.")


if __name__ == '__main__':
    email = input("Please input your email address: ")
    check(email)
