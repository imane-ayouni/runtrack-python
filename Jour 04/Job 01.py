number = input("Choose a number ")
def factorial(number):
    if number == 1:
        return 1
    else:
        return (int(number) * factorial(int(number)-1))
print("The factorial of ", number, " is ", factorial(number))