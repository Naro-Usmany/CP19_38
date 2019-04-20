row=10
a=0
b=7
for j in range(1,row,2):
  for k in range(row-1,j,-2):
    print(" ",end=" ")
  for i in range(0,j):
    if(i+1==j-i):
      print(a,end=" ")
    elif(j+1==row):
      print(a,end=" ")
    else:
      print(b,end=" ")
  print(" ")
for j in range (row-1,0,-2):
  if(j!=row-1):
    for k in range(j,row-1,2):
      print(" ",end=" ")
    for i in range(0,j):
      if(i+1==j-i):
        print(a,end=" ")
      else:
        print(b,end=" ")
    print(" ")