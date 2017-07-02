#!/usr/bin/python
var=1
fo = open("foo1.txt", "w")
while var==1:
 str=raw_input("enter the data:")
 fo.write(str);
 print "Read String is : ", str
# Close opend file
fo.close()

