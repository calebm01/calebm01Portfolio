#Caleb Mouritsen
#9/13/18
#get name function

#def get_name():

#ask user for name
    #name = input("what is your name?: ")
#verify name
    
#display name
#print("the name you entered was", name)



#print("this is our function")
#get_name()


#Finding the area of a circle

def AreaofCircle(radius1):
    
    pi = 3.14159265

#1 get a radius
    radius = radius1
#2 compute the area
    radius = float(radius)
    area = radius*radius*pi
#3 display the area
    print("the area of the circle is: ", area)
    radiusx=input("what is the radius")
    AreaofCircle(radiusx)
