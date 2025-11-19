## CH4, python for everybody  Math functions
import math
print(math)
radians=0.7
height= math.sin(radians)
print(height)
#random numbers
import random #this module provide functions that generate pseudorandom numbers

for i in range (10):
    x= random.random()
    print("valor ", i, " es: ",  x)

#.randint(n, k) returns an integer between low (n) and high (k)
print("the random number between 1 and 111 is: ", random.randint(1,111))

# random.choice(n) selects an element from a sequence at random
t= [1 , 2 ,3]
T= (1 , 2 ,3)
print(t)
print(type(t))
print(T)
print(type(T))
print(random.choice(t))
print(random.choice(T)) #funciona con listas y tuplas

#Adding new functions

def print_classic():      #Header
    print("Hello world!") #Body

print(print_classic)
print(type(print_classic)) #Defining a function creates a variable with the same name

#REMEMBER THE FLOW OF EXECUTION

#%% Exercises chapter 4.14

#EX6: Rewrite your pay computation with time-and-a-half for over-time and create a 
#function called computepay which takes two parameters (Hours and Rate)

def computepay(a, b):
    hours=float(a)
    rate=float(b)
    if hours>40:
        over_hours= hours-40
        totalpay= ((hours-over_hours)*rate)+(over_hours*(rate*1.5))
        print(totalpay)
    else:
        totalpay=hours*rate
        print(totalpay)
        
parameter_a=float(input("Enter the amount of hours worked: "))
parameter_b=float(input("enter the normal rate per hour: "))
computepay(parameter_a, parameter_b)

def grade(a):
    a=float(a)
    if a>=0.9:
        print("Grade: A")
    elif a>=0.8:
        print("Grade: B")
    elif a>=0.7:
        print("Grade: C")
    elif a>0.6:
        print("Grade: D")
    else a0.6:
        print("Grade: F")
