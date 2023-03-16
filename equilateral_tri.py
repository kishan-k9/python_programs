n=5
for i in range(1,n):
  for j in range(1,n):
    if j>=(n+1)-i & j<=(n-1)+i:
        print(" *")
    else:
        print(" ")
    print("\n")