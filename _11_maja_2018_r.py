import enum
from re import A


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
from string import ascii_uppercase
from math import fabs
Alphabet=list(ascii_uppercase)
ws1=[]
for word in words:
    c=0
    for l1 in word:
        for l2 in word:
            if fabs(Alphabet.index(l1)-Alphabet.index(l2))>=10:
                c+=1
    if c==0:
        ws1.append(word)
for i in ws1:
    print(i)