# Excercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
h=float(input("enter the worked hours: "))
rate=float(input("enter the normal rate per hour"))

if h>=40:
  extra_h= h-40
  extrapay=(h*rate)+(extra_h*1.5*rate)
  print("Pay: ", extrapay)
else:
  pay=h*rate
  print("Pay: ", pay)


  
  
