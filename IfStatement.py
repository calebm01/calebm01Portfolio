name = input("what is your name")
age = input("what is your age")


if name.isalpha() and name.istitle() and age.isdigit() and age<"25" or name == "Balthazar, immune to blade and arrow":
    print("The name you entered was:", name + ",", "your age was", age)
else:
    print("Sorry, you aren't cool enough")
