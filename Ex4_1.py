import random

#random returns a pseudo random number 0.0 <= x < 1.0
for i in range(10):
    x = random.random()
    print x
    
#randint takes parameters low and high and returns an integers
#low <= x <= high
for i in range(5):
    y = random.randint(5,10)
    print y

#To choose an element from a sequence at random, use choice
t = [1, 2, 3]
print random.choice(t)    

#random also has gaussian, exponential, gamma, and a few other distributions
