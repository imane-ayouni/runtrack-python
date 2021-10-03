question_1= input("Type a number: ")
question_2= input("Type a second number: ")
question_3= input("Type a third number: ")
question_4 = input("Type a fourth number: ")
question_5= input("Type a fifth number: ")
numbers_list= [question_1,question_2,question_3,question_4,question_5]
sorted_numbers= sorted(numbers_list)
print("Your numbers in an ascending order are: "+str(sorted_numbers))