#prompt user for numbers to calculate 
first = input("first number: ")
operator = input("operator:")
second = input("second number: ")

#for multiplication
if operator == "*":
    answer = (float(first) * float(second))
    print("answer: " + str(answer))
    
#for addition
elif operator == "+":
    answer = (float(first) + float(second))
    print("answer: " + str(answer))
    
#for subtraction
elif operator == "-": 
    answer = (float(first) - float(second))
    print("answer: " + str(answer))
#for division
elif operator == "/": 
    answer = (float(first) / float(second))
    print("answer: " + str(answer))