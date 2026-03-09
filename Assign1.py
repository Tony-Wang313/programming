# Question 1

# Task 1 - Coding
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == '__main__' :
    number=float(input("Enter your number:"))
    print (check_number(number))

# Task 2 - Understanding
# The input is a float number. 
# The output is one of the following word: "Positive", "Negative", or "Zero". 
# The variable is that represent the input is "number".
# There is a user-defined function named "check_number(number)".
# There is a built-in function float() to convert the input into decimal nimber.
# There is the built-in function print() to write the output returned from the user-defined function.

# Task 3 - Modification

def check_number(number):
    if number > 0:
        return str(number) + " is positive." 
    elif number < 0:
        return str(number) + " is negative."
    else:
        return str(number) + " is zero."
    
if __name__ == '__main__' :
    number=float(input("Enter your number:"))
    print (check_number(number))

#Improve output formatting    
# A built-in function str() which converting the input into text is added in the return statement.
# Therefore, the ouput is a full sentence that recall the entered number and that check if it is positive, negative or zero.

# Question 2

# Task 1 - Coding
def star_shape(rows):
    shape = ""
    for i in range(1, rows + 1):
        shape += "*" * i + "\n"
    return shape.strip()

if __name__ == '__main__' :
    rows=int(input("Enter the amount of rows:"))
    print (star_shape(rows))

# Task 2 - Understanding
# The input is the value of the  amount of rows that are in the shape. 
# The output is a rectangle triangle formed by stars "*". The first row has only one star, each row have one more until it have the amount of rows inputted.
# The variable is that represent the input is "rows".
# There is a string variable "shape" that represent the compilation of stars' rows.
# There is a user-defined function named "star_shape(rows)".
# There is a built-in function int() to convert the input into integer because the number of row cannot be a decimal number.
# There is a built-in function range() to create a sequence of numbers from 1 to "rows" + 1 which are the number of start for each row.
# There is the built-in function print() to generate the triangle of stars returned from the user-definition function.

#Task 3 - Modification
def star_shape(rows):
    for i in range(1, rows + 1):
       print (i * "*")
    
if __name__ == '__main__' :
    rows=int(input("Enter the amount of rows:"))
    star_shape(rows)
# Alter calculation logic
# Instead of using the line of shape+=(...) to store the output, it directly print the output (which is no more stocked in the function).
# The line are directly changed because it is a for loop.

# Question 3

# Task 1 - Code
def count_multiples_of_3(limit):
    num = 1
    result = ""
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip()

if __name__ == '__main__' :
    limit=int(input("Enter the limit: "))
    print(count_multiples_of_3(limit))

#Task 2 - Understanding
# The input is the last number of the list of integer from 1.
# The output is a column of number that count from one to the input value, and for each multiple of 3, the number is replaced by the words "Multiple of 3".
# The variable that represent the limit is "limit".
# "num" is the counter variable of the loop. It keeps track of which number the function is currently processing.
# "result" is a string variable that store the output. Each number or "Multiple of 3" is added this string with a new line.
# There is a user-defined function named "count_multiples_of_3(limit)".
# There is a built-in string method str() to delete the last empty line create by " result += str(num) + "\n" " for the last number in the serie.
# There is a built-in function int() to convert the value of the input into an integer.
# There is the built-in function str() to convert the value of num (the numbers in the list from 1 to "limit") into a text form that can be outputted.\
# There is a built-in function print() to generate the output returned from the user-definition function.

#Task 3 - Modification
def count_multiples_of_3(limit):
    if limit <1 :
        return "Invalid limit"
    num = 1
    result = ""
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip()

if __name__ == '__main__' :
    limit=int(input("Enter the limit: "))
    print(count_multiples_of_3(limit))

# Add validation
# The first If statement make sure that it is possible to have a list of number with the given input.
# It reject all the negative values and zero (smaller than 1)

# Question 4

# Task 1 - Coding:
def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total

if __name__ == '__main__' :
    start=int(input("Enter the first number: "))
    end=int(input("Enter the last number: "))
    print(sum_of_even_numbers(start, end))

# Task 2 - Understanding
# There are two inputs: The first number from which start the series of number in which it took the even number to calculate the sum. The last number of that list.
# The output is the sum of all the even number in the range determined by the two inputs.
# The variable that represent the first number is "start". The variable that represent the last number is "end".
# There is a user-defined function named "sum_of_even_numbers(start, end)".
# There is a built-in function int() to convert the value of the input into an integer, so the range is defined between two numerical value.
# There is a built-in function range() to create a sequence of numbers from "start" to "end", from whcih even number are summed.
# There is a built-in function print() to generate the output in the 

# Task 3 Modification
def sum_of_even_numbers(start, end):
    equation=""
    multiples =[]
    line = ""
    for num in range(start, end + 1):
        if num < end - 1:
            if num % 2 == 0:
                multiples.append(int(num))
                line+= str(num)+"+"
        elif num == end-1:
            if num % 2 ==0:
                        multiples.append(int(num))
                        line+=str(num)+"="
        elif num == end:
            if num % 2 ==0:
                        multiples.append(int(num))
                        line+=str(num)+"="
        total=sum(multiples)
    equation += line + str(total)
    return equation

if __name__ == '__main__' :
    start=int(input("Enter the first number: "))
    end=int(input("Enter the last number: "))
    print(sum_of_even_numbers(start, end))

# Add new feature
# Instead of only ouputting the result of the sum, the new code output also the equation which is "first even number"+"second even number"+...+"last even number"="sum of all even numbers"
# A list called "even" with all the even number is created while the code process. 
# Each time "num" == even number in range, int(num) is added to the list and str(num) is added to the line that represent the sum equatiob with a "+" symbol .
# At the even last number "num"(either end or end - 1), int(num) is stored in the list, and instead of a "+" sign, a "=" sign is added to the line, because the equation is ending and the total is going to be calculated.
# The total is then calculated wiht a sum() fucntion.