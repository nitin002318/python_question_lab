word,n = input("\nEnter a word and value of n :  ").split()

if len(word)<2 :
    print("\nInvalid Input")

else :
    n = int(n)
    a = word[-n:]
    b = word[:-n]
    print(a+b)f=open('sample.txt','r')
str=f.read()
print(str)
f.close
