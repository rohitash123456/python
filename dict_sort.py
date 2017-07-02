"""
if __name__ == '__main__':
    a= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]
    
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])
"""


"""if __name__ == '__main__':
    a= []
    for _ in range(int(input())):
#        name = input()
        score = int(input())
        a.append(score)
    a.reverse()
    print(a)
    m=0
    for x in a:
	if x>m:
	  m=x
    print(m)
    for x in a:
         if x<m:
           print(x)
           break
   """ 
#if __name__ == '__main__':
a=[]
n=int(input())
for x in range(n):
    score = int(input(""))
    a.append(score)
a.reverse()
#print(a)
m=0
for x in a:
    if x>m:
        m=x
#print(m)
for x in a:
    if x<m:
     print(x)
     break




"""N = int(raw_input())
students = []
for i in xrange(N):
    grade = [raw_input(), float(raw_input())]
    students.append(grade)    
students = sorted(students, key=lambda x: x[1])
second_highest = students[0][1]
for name, grade in students:
    if grade > second_highest:
        second_highest = grade
        break
print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))
"""
"""
y=dict()
x=list()
#if __name__ == '__main__':
n=int(input())
for _ in range(n):  #(int(input())):
        name=raw_input("enter name:")
        score=float(input("enter marks:"))
        y[name]=score
print(y)
#for in range(n):
c=y.values()
sec=sorted(list(set(c)))
for key,values in y.items():
		x.append([values,key])
x.sort()
x.reverse()
print(x)
m=10
for a in x:
	if a<m:
           m=a
print(m)"""

