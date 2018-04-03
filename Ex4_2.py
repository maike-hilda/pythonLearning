#Exercise 4.2 and 4.3
#def print_lyrics():
#    print "I'm a lumberjack, and I'm okay."
#    print 'I sleep all night and I work all day.'
#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
#repeat_lyrics()

#Move the last line to the top, what happens? 
#--> Repeat lyrics is not defined

#Move the definition of print_lyrics after the definition of repeat_lyrics
#What happens? 
#--> Gets executed the same way it would if the order wasn't changed
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print 'I sleep all night and I work all day.'
repeat_lyrics()