#!/usr/bin/python

fo = open("foo.txt", "r+")
str = fo.read();
print "Read String is : ", str
pos=fo.tell()
print pos
fo.seek(0,0)

print pos
# Close opend file
fo.close()

