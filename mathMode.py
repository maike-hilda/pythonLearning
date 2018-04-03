import math
#Use print math to get some info on the module object math

logTen = math.log10(1000) #calculates the log base 10
print logTen 
logE = math.log(10) #calculates the log base e 
print logE 

radians = 0.7
y = math.sin(radians)
print 'The sine of 0.7 equals ' + str(y)

degrees = 45
radians = degrees * math.pi / 180 #pi is accuarate to ~15 digits
x = math.cos(radians)
print 'The cosine of ' + str(degrees) + ' degrees equals ' + str(x)

#What base and exponent would you like to use as parameters?
b = 5
e = 3
number = math.pow(b,e)
print number 


