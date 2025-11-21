largest = None
iteration_num=0
print('Before: ', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar> largest:
        largest= itervar
    iteration_num=iteration_num+1
    print('Iteration number: ', iteration_num, 'itervar value:', itervar, 'Largest until now:', largest)
print('largest: ', largest)

#%%EXERCISES CH 5
# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done"
# Once "done" is entered, print out the total , count,
# and average of the numbers. If the user enters anything other than a 
# number, detect their mistake using try and except and print an error message and skip to the next number


