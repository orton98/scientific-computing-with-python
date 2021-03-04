# Rewrite the program that prompts the user for a list of numbers and prints out
# the maximum and minimum of the numbers at the end when the user enters "done".
# Write the program to store the numbers the user enters in a list and use the
# max() and min() functions to compute the maximum and minimum numbers after the
# loop completes.


if __name__ == '__main__':
    numbers =  []
    while True:
        n = input()
        if n == "done":
            break
        else:
            numbers.append(int(n))
    print("Maximum: "+str(max(numbers)))
    print("Minimum: "+str(min(numbers)))
