##Write a program to prompt the user for their name and then welcomes them.
while True:
  name=input("Please write your name: ").strip()
  if not name:
    print("No name was added, please add a name ")
  elif name.isdigit():
    print("The name you wrote is a number, please enter a valid name")
  else:
    print("Hello: ",name)
    break
##Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
## Enter Hours: 35, Enter Rate: 2.75, Pay: 96.25
while True:
  try:
    hours=float(input("Please enter amounts of hours worked: "))
    rate=float(input("Please enter rate per hours: "))
    if hours <=0:
      print("Enter a valid amount of hours")
    elif rate <=0:
      print("Enter a valid rate")
    else:
      pay=rate*hours
      print("Pay: ", pay)
      break
  except:
    print("Please enter a valid hour or rate")
##Exercise 4 Assume that we execute the following assignment statments: width= 17, height=12.0
  width=float(17)
  print(type(width))
  height=12.0
  print(type(height))
  e1=width//2
  print(e1)
  e2=width/2
  print(e2)
  e3=height/3
  print(e3)
  e4=1+(2*5)
  print(e4)
  
    
