import enum


file= open("przyklad.txt", "r")
print(file)
words=list(map(str.strip, file.readlines()))
#print(words)
k=1
z1=""
for i in range(len(words)):
    if i+1==k*40:
        for n,j in enumerate(words[i]):
            if n==9:
                z1+=j
        k+=1
print(z1)
#4.2
l=[]
nd=0
ndw=""
for word in words:
    for letter in word:
        l.append(letter)
    s=set(l)
    if len(s)>nd:
        nd=len(s)
        ndw=word
    l=[]
print(nd, ndw)