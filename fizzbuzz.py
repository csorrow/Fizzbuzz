import sys

if len(sys.argv) <= 1:
    end = (raw_input("Enter Ending Number:  "))
else:
    end = (sys.argv[1])

# print number
# print type(number)
    
# end = int(number)
# print type(end)

# #### NEED TO WALK THROUGH THIS WITH VICTOR

while type(end) != int:      
    try:
        end = int(end)  ##Added this and it worked, but took a long time to figure out
    except ValueError:
        end = raw_input("Please Enter Integer:  ")
        


#print end      
end = end + 1
begin = 1
div1 = 3
div2 = 5
numbers = range(begin,end)

#print ls

for number in numbers:
    if number % div1 == 0 and number % div2 != 0:
        print 'Fizz'
    elif number % div1 != 0 and number % div2 == 0:
        print 'Buzz'
    elif number % div1 == 0 and number % div2 == 0:
        print 'FizzBuzz'
    else: 
        print number    


# import sys
# print sys.argv[1]

# print "The name of this script is {}".format(sys.argv[0])
# print "User supplied {} arguments at run time".format(len(sys.argv))

# for arg in sys.argv[1:]:
#   print arg
