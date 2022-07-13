n=int(input("how many lines you want to in star pattern:-"))

for i in range(n):
     m=1
     for j in range(i+1):
          print(m,end=' ')
          m=m+1
     print("\n")