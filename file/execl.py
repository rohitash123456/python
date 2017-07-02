import sys 
"""print("name",sys.argv[0])
print("len",len(sys.argv))
print("argument",str(sys.argv))"""
f=open("xxx.csv","w+")
f.write("first_name,last_name\n")
while 1:
	str=raw_input("enter first name:")
	if str in "QUIT":
		break
	f.write(str)
	f.write(",")
	str=raw_input("enter last name:")
	if str in "QUIT":
		break
	f.write(str)
	f.write("\n")
f.close()

