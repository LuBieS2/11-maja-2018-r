n=4
X=[1, 2, 3, -2]
Y=[3, 1, 4, 2]
Xu=[]
Yu=[]
x=X[0]
y=Y[0]
for i in range(n):
        if X[i]/Y[i] < x/y:
            x=X[i]
            y=Y[i]
print(x, y)
#2.2
for j in range(n-1):
    for i in range(n-1):
        if X[i+1]/Y[i+1] < X[i]/Y[i]:
            t=X[i]
            X[i]=X[i+1]
            X[i+1]=t
            t=Y[i]
            Y[i]=Y[i+1]
            Y[i+1]=t
print(X, Y)