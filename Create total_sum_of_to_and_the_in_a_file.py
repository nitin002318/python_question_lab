f=open('avin.txt','r')
f.seek(0,0)
str=f.read()
print(str)
b=str.lower()
print(b)
b=b.split()
print(b)
sum=0
for i in b:
    if i =='to' or i=='and' or i=='the':
            sum+=1
print(sum)
f.close()
