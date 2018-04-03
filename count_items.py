#Count items in a loop
nums = [3, 41, 12, 9, 74, 15]
count = 0
for itervar in nums: #itervar is the iteration variable
    count = count + 1
print 'Count: ', count

#Add up items in a loop
total = 0
for itervar in nums:
    total = total + itervar
print 'Total: ', total 

#But there are built-in functions for this

print 'Count: ', len(nums)
print 'Total: ', sum(nums)

