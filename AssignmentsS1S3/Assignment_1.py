# problem statement 1
def find_sum():
    num =  input("enter a number : ")
    sum = 0
    try:
        for char in num:
            sum += int(char)
        print(f"for input {num}, sum of digits : {sum}")
    except ValueError as err:
        print("value entered is not an integer")

# problem statement 2
def check_armstrong():
    num =  input("enter a number to check if it armstrong: ")
    order =  len(num)
    sum = 0
    try:
        for char in num:
            sum += pow(int(char), order)
        print(f"for input {num}, sum of digits : {sum}")
        if int(num) == sum:
            print(f"number {num} is an armstrong number")
        else:
            print(f"number {num} is not an armstrong number")
    except ValueError as err:
        print("value entered is not an integer")

# problem statement 3
def check_palindrome():
    string_check =  input("enter a string to check if it is palindrome: ")
    if string_check == string_check[::-1]:
        print(f"{string_check} is palindrome")
    else:
        print(f"{string_check} is not palindrome")
    
if __name__ == "__main__":
    # find_sum()
    # check_armstrong()
    check_palindrome()