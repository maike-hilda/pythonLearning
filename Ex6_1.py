#Exercise 6.1
#Write a while loop that starts at the last character in the string
#and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.

word = 'bananas'
count = len(word)-1
while count >= 0:
    print word[count]
    count = count - 1    