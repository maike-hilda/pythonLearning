#Exercise 5.2
#Write another program that prompts for a list of numbers as above
#and at the end prints out both the max and min of the numbers instead
#of the average.
count = 0
total = 0
maxi = None
mini = None 
while True:
    number = raw_input('Enter a number:')
    if number == 'done':
        break 
    try:
        number = float(number)
    except:
        print 'Invalid input'
        continue
    if maxi is None or maxi < number:
        maxi = number
    if mini is None or mini > number:
        mini = number
    count = count + 1
    total = total + number 
print total, count, maxi, mini     
    
    