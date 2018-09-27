##age = int(input("what is your age: "))
##
##if age < 65 or age < 16:
##    print("You can drive")
##elif age > 65:
##    print("you can't drive loser, you're blind")
##elif age < 16:
##    print ("you can't drive loser, you need to wait")
##else:
##    print("are you ok?, put in a number")

##num1: input from thse user; cast to int
##num2: input from the user; cast to int
##
##check numbers if num1 and num2 are all digits
##if both are digits tell user (compound if)
##if one or the other is a digit tell user
##if neither are digits tell user

num1 = input("enter a number")
           
num2 = input("enter a number")

if num1.isdigit() and num2.isdigit():
    print(num1,num2,"are both digits")
elif num1.isdigit() or num2.isdigit():
    print("only one of the numbers is a digit")
else:
    print("those are not digits")


    
    
