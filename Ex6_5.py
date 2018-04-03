#Exercise 6.5
str = 'X-DSPAM-Confidence: 0.8475'
#Use find and string slicing to extract the portion of the string
#after the colon character and then use the float function to convert
#the extracted string into a floating point number

first = str.find(' ')
second = len(str)
num = str[first+1:second]
fnum = float(num)

print 'The desired number is %g' % fnum