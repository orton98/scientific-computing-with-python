# Function to return the square root of
# a number using Newtons method
def squareRoot(n, l):
    # Assuming the sqrt of n as n only
    x = n

    # To count the number of iterations
    count = 0

    while (1):
        count += 1

        # Calculate more closed x
        root = 0.5 * (x + (n / x))

        # Check for closeness
        if (abs(root - x) < l):
            break

            # Update root
        x = root

    return root