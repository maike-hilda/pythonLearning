#Chapter 6 random

fruit = 'banana'
letter = fruit[1] #1 is called the index
print letter #here 'a'

length = len(fruit)
lastLetter = fruit[length-1]
#or the same result doing the following
lastLetterAlt = fruit[-1]
print lastLetter, lastLetterAlt 

print 'Using a while loop:'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1

print 'Using a for loop:'    
for char in fruit:
        print char 
        
#Slices of strings
s = 'Monty Python'
print s[0:5] #excludes the last character
print s[6:12]        

print fruit[:3]
print fruit[3:]
print fruit[3:3] #prints an empty strings
print fruit[4:2] #empty string 
print fruit[:]

#count the letter a

count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print 'The letter a shows up', count, 'times'

#in as a boolean operator
print 'a' in 'banana' #prints True
print 'seed' in 'banana' #prints False  

print fruit.capitalize() 
print fruit 
    
    






