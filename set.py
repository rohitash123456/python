t=int(input("enter test case:"))
y=list()
s=list()
for x in range(t):
  str=raw_input("enter string:")
  y.append(str)
for x in y:
  if x not in s: 
    s.append(x)
s.sort()
print(s)  
