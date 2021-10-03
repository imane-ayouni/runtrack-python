def num_list():
    the_list = []
    number = 0
    for number in range(1, 100):

        if number % 3 == 0:
            number = str("Fizz")
        elif number % 5 == 0:
            number = str("Buzz")
        elif (number % 3 and number % 5) == 0:
            number = str("FizzBuzz")

        the_list.append(number)
    return the_list
final_list = str(num_list())
print(final_list)