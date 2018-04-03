#Exercise 5.1
#Write a program which repeatedly reads numbers until the user enters
#"done". Once "done" is entered, print out the total, count, and average
#of the numbers. If the user enters anything other than a number, detect
#their mistake using try and except and print and error message and skip
#to the next number

count = 0
total = 0
while True:
    number = raw_input('Enter a number:')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print 'Invalid Input'
        continue 
    count = count + 1
    total = total + number
if count != 0: #to assure no error if user does not enter any numerial values at all 
    average = total / count  
    print total, count, average 
    