#Parsing strings
data = 'From stephen.marquard@utc.ac.z Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print atpos
sppos = data.find(' ', atpos)
print sppos 
host = data[atpos+1:sppos]
print host

#Format operator %
#formats an integers as a string 
camels = 42
print '%d' % camels #prints the string 42 

print 'I have spotted %d camels.' % camels

