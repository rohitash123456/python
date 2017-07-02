y=list()
t=int(input(""))
for _ in range(t):
        s=0
	cnt=0
	n=int(input(""))
	cnt=cnt+1
	if n==1:
		f=(int(input("")))
		print("Case %d",cnt)
	else:
	 for _  in range(n):
	     i=int(input(""))
	     if i%2!=0:
                s=s+i           
      	 print("Case",cnt,":",s)
 
	
