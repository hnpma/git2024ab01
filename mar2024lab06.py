#11:10 AM 3/14/2024
#
'''
e Big Exercise: Number Manipulation
In this lab you'll make a single large program that uses several function definitions. Your main will be in charge of using the other functions you define.

What your program will do is present the user with the following menu:

1) Count digits
2) Sum digits
3) Is Palindrome
4) Reverse 
5) Exit
Choice: 
Option	Behavior
Count digits	Prompt the user for a positive int and count how many digits are in that number
Sum digits	Prompt the user for a positive int and sum up all the digits in that number
Is Palindrome	Prompt the user for a positive int tell whether or not their number is a palindrome
Reverse	Prompt the user for a positive int and print the reverse of the number
Exit	Exit the program
For all choices, you may assume good input.

Type Requirement
You must store the user's input as an int for the duration of the program.
You cannot use string methods to manipulate the digits.
You will not be responsible for number with leading or trailing zeroes, but zeroes can be in the middle (e.g. 12021)
Required Functions
You will write several functions that you will use in combination to complete this lab:

last_digit(num)
returns the last digit in n
example last_digit(123) returns 3
remove_last_digit(num)
returns the number n with the last digit trimmed off
example remove_last_digit(123) returns 12
when remove_last_digit is passed a 1-digit number, return 0
add_digit(current_num, new_digit)
returns the current_num with new_digit placed into the ones space
example add_digit(123, 4) returns 1234
reverse(num)
returns the reverse of num
example reverse(1234) returns 4321
this function should call other functions you've defined
is_palindrome(num)
returns true if num is a palindrome
example is_palindrome(12321) returns True, but is_palindrome(123) returns False
This should use reverse
count_digits(num)
returns the count of digits in num
example count_digits(123) returns 3
this function could be helped by remove_last_digit
sum_digits(num)
returns the sum of digits in num
example count_digits(123) returns 6
this function should use last_digit and remove_last_digit
print_menu()
prints the menu
This does NOT obtain user input, it only prints the menu
main
Until the user wants to quit, this main will print the menu, obtain the user's choice, and call the appropriate functions to print the desired results
EECS 169 Exercise: Prime detector
You must add one additional menu item (before exit when printing) to detect if the number given by the user is prime or not. You must define and use a function called...

is_prime(num)
Determines if num is prime or not
NOTE:

there are not points for efficiency for this one.
'''
def is_prime(number):
  if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range (2,number):
      if (number % i) == 0:
        is_prime_number = True
        break
if is_prime_number:
  return ("The number you have entered is not a prime number")

else:
  return (" The number you have entered is a prime number")



def last_digit(num):
  lastDig = num % 10
  return lastDig

def remove_last_digit(num):
  newNum = int(num/10)
  return newNum

def add_digit(current_num, new_digit):
  newNum = (current_num*10)+new_digit
  return newNum

def reverse(num):
  firstDig = last_digit(num)
  for i in range(count_digits(num)-1):
    num = remove_last_digit(num)
    revNum = add_digit(firstDig, last_digit(num))
    firstDig = revNum
  return firstDig


def is_palindrome(num):
  back = reverse(num)
  if back == num:
    return True
  else:
    return False
def count_digits(num):
  count = 0
  while num!= 0:
    num //= 10
    count+=1
  return count
def sum_digits(num):
  sum = 0
  num2 = num
  count = count_digits(num)
  for i in range (count):
    sum += last_digit(num2)
    num2 = remove_last_digit(num2)
  return sum

def print_menu():
    print()
    print('Enter a number between 0 to 6')
    is_prime(number)
    print(' 1) Count digits\n 2) Sum Digits\n 3) Is Palindrome\n 4) Reverse\n 5) Exit')
def main():
  print_menu()
  choice = int(input('Choice (enter 1-5):'))
  while choice != 5:
    number = int(input('Give me a positive integer:' ))
    if choice == 1:
      print('The number of digits in your number is :   '+str(count_digits(number)))

    elif choice ==2:
      print('The sum of digits in your number is: '+str(sum_digits(number)))
    elif choice == 3:
        if is_palindrome(number) == True:
            print('The number you entered is a Palindrome')
        else:
           print('The number you entered is not a Palindrome')
     # print('Your number being a palindrome is: '+ str(is_palindrome(number)))
    elif choice == 4:

      print('Your number in reverse is: '+ str(reverse(number)))
    print()
    print_menu()
    choice = int(input('Choice (enter 1-5):'))

  if choice ==5:
    print('Exiting program')

main()
