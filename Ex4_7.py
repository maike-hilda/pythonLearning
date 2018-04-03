#Exercise 4.7
#Rewrite the grade program from the previous chapter using a function
#called computergrade that takes a score as its parameter and returns
#a grade as a string.

def computergrade(score):
    if score > 1 or score < 0 or type(score) == 'str':
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
        
#Testing
score = raw_input('Enter score:\n')
try:
    score = float(score)
except:
    pass 
   
computergrade(score)
        
