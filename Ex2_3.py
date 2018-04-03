#Exercise 2.3
#Write a program to prompt the user for hours and rate per hour to
#compute gross apy.
hours = raw_input('Enter hours:\n')
rate = raw_input('Enter rate:\n')
try: 
    rate = float(rate)
    hours = float(hours)
except:
    print 'Please enter numbers.'
    
pay = hours*rate

print 'Pay: ' + str(pay) #must convert to be able to concatenate


