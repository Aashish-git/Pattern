n=int(input("how many lines you want to in star pattern:-"))

m=(2*n)
for i in range(n):
     for j in range(m-i):
          print(" ",end='')
     for j in range(i+1):
          print("*",end='')
     print("")