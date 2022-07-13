n=int(input("how many lines you want to in star pattern:-"))

m=(2*n)-2

for i in range(n):
     for j in range(m):
          print(" ",end='')
     m=m-1
     for j in range(i+1):
          print("* ",end='')
     print("")