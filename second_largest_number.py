
#if __name__ == '__main__':
a=[]
n=int(input())
for x in range(n):
    score=int(input())
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



