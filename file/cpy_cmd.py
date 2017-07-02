import sys
f=open(sys.argv[1],"r")
f1=open(sys.argv[2],"w+")
s=f.read()
f1.write(s)
print(s)
f.close()
f1.close()
