x=int(raw_input(""))
y=int(raw_input(""))
z=int(raw_input(""))
n=int(raw_input(""))
l=list()
"""for a in range(x):
    for b in range(y):
       for c in range(z):
        print(x)#,y,z)
 	print(y)
        print(z) """


print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n])   
