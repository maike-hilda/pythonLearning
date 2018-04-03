#Exercise 6.3
#Write a function named count that accepts a string and a letter to 
#be counted as an argument

def count(word, countLetter):
    count = 0
    for letter in word:
        if letter == countLetter:
            count = count + 1
    print 'The letter', countLetter, 'appeared', count, 'times.'
        