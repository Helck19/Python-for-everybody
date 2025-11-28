# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
index=0

while True:
    try:
       word=str(input("Please input the desired word: "))
    except:
        print("Please add a string")
        continue
    while index<len(word):
        reverse=word[(-1)*(index+1)]
        print(reverse)
        index=index+1
    control=input("Do you wish to do it again with another word? type yes or no:  ")
    control=control.lower()
    if control=="yes":
        index=0
        continue
        
    elif control=="no":
        break
#%%String slicing
s="Monty python"
print(s[0:5])
print(s[6:])
print(s[:len(s)])
print(type(s[:]))
print(s[:])

#Strings are inmutable

greeting= "Hello, world"
new_greeting=greeting[:5]+" python and"+greeting[6:]
print(new_greeting)

#Excercise 3: Encapsulate this code in a function named, count, and generalize it so that it accepts the string and the letter as arguments.

def count(word, letter_to_find):
    count=0
    for letter in word:
        if letter==letter_to_find:
            count=count+1
    print("Amount of letter", letter_to_find, "found are: ", count)
        

count("banana", "a")

#%%Counting letters in a word
word=input("Please enter the word that you wish to count the letters: ").lower()

for i in set(word):
    count=word.count(i)
    print("The number of times the letter: ", i, "appears in the word", word,"is: ", count)

#%%Exercise 5: Take the following Python code that stores a string:
string= 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after
#the colon character and then use the float funciont to convert the extracted
#string into a floating point number.
index=string.find(":")
number=float(string[index+1:])
print(number)



  
