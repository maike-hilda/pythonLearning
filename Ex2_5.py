#Exercise 2.5
#Write a program that prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted
#temperature
#Note: 0 deg C equals 32 deg F and 1 C increase equals 9/5 F increase
C = raw_input('Enter the current temperature in Degree Celcius:\n')
try:
    C = float(C)
except:
    print 'Please enter a number.'
    
F = C * 9/5 + 32

print 'The current temperature is ' + str(F) + ' degree Fahrenheit'
