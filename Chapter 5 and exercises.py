# largest = None
# iteration_num=0
# print('Before: ', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar> largest:
#         largest= itervar
#     iteration_num=iteration_num+1
#     print('Iteration number: ', iteration_num, 'itervar value:', itervar, 'Largest until now:', largest)
# print('largest: ', largest)

#%%EXERCISES CH 5
# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done"
# Once "done" is entered, print out the total , count,
# and average of the numbers. If the user enters anything other than a 
# number, detect their mistake using try and except and print an error message and skip to the next number

total=0
count=0
while True:
    inp=input("Enter number: ")
    if inp.lower()=="done":
        break
    try:
        num=float(inp)
    except:
        print("Enter a valid input: ")
        continue
    total=total+num
    count=count+1
    average=total/count
    
    if count>0:
        average=total/count
    else:
        average=0
print("Total:", total, " Count:", count, " Average:", average )

#%%EXERCISE CH 5
# Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and the minimum of the 
# numbers instead of the average.

print("This time it gives maximum and minimum")

lista=[]
while True:
    inp=input("Enter number: ")
    if inp.lower()=="done":
        break
    try:
        num=float(inp)
    except:
        print("Enter a valid input: ")
        continue
    lista.append(inp)
maximo=max(lista)
minimo=min(lista)
print("Maximo: ", maximo, "Minimo: ", minimo)
