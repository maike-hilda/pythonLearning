#Exercise 4.6
#Rewrite your pay computation with time-and-a-half for overtime
#and create a function called computepay which takes 
#two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        pay = ( 40 + ( hours - 40) * 1.5 ) * rate
    else:
        pay = hours * rate
    return pay
    
h = raw_input('Enter Hours:\n')
r = raw_input('Enter Rate:\n')
try:
    h = float(h)
    r = float(r)
except:
    print 'Please provide numerical inputs only'
    
p = computepay(h, r)
print p 
    