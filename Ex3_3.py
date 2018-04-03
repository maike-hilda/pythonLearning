#Exercise 3.3
#Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error message.
#If the score is between 0.0 and 1.0, print a grade using the following
#table (omitted, just regular grade scale in college)

score = raw_input('Enter score: \n')

try:
    score = float(score)
except:
    print 'Bad score'

if score > 1 or score < 0:
    print 'Bad score'
elif score >= 0.9:
    print 'A'
elif score >= 0.8:
    print 'B'
elif score >= 0.7:
    print 'C'
elif score >= 0.6:
    print 'D'
else:
    print 'F'
    