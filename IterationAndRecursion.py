# WK8Lab1 - Iterative and Recursive Functionality Lab Submission
# This program demonstrates the functionality of the factorial function.
# Course no: CIS 261
# Name: Terrence Miller


# factorial function by iteration
def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# Facorial function by recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    print("Factorial results using an iterative function")
    print("0! = ",factorial_iter(0))
    print("5! = ",factorial_iter(5))
    print("10! = ",factorial_iter(10))
    print("25! = ",factorial_iter(25))
    print("50! = ",factorial_iter(50))
    print("100! = ",factorial_iter(100))

    print("Factorial results using a recursive function")
    print("0! = ",factorial(0))
    print("5! = ",factorial(5))
    print("10! = ",factorial(10))
    print("25! = ",factorial(25))
    print("50! = ",factorial(50))
    print("100! = ",factorial(100))

if __name__ == "__main__":
    main()

