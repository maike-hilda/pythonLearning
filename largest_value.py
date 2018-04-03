#Find largest value in a list or sequence
largest = None
print 'Before:', largest
nums = [3, 41, 12, 9, 74, 15]
for itervar in nums:
    if largest is None or itervar > largest:
        largest = itervar
    print 'Loop:', itervar, largest
print 'Largest:', largest 

#Find the smallest value in a list or sequence
smallest = None 
print 'Before:', smallest
for itervar in nums:
    if smallest is None or smallest > itervar:
        smallest = itervar
    print 'Loop:', itervar, smallest
print 'Smallest:', smallest 

#or use a built-in function
print 'From the built-in functions we get:'
print 'Smallest:', min(nums)
print 'Largest:', max(nums)