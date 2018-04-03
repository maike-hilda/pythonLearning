#Exercise 3.1 and 3.2
#Rewrite your pay computation to give the employee 1.5 times the
#hourly rate for hours worked above 40 hours
#use try and except

hours = raw_input('Enter Hours:\n')
rate = raw_input('Enter Rate:\n')

try:
    hours = float(hours)
    rate = float(rate)
except:
    print 'Error, pleae enter numeric input'

if hours > 40:
    pay = ( 40 + (hours - 40) * 1.5 ) * rate
else:
    pay = hours * rate
    
print 'Pay: ' + str(pay)    
  
    