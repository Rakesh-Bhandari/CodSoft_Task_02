import sys

def add(a,b):
 sum=a+b
 return sum

def sub(a,b):
 difference=a-b
 return difference

def mult(a,b):
 product=a*b
 return product

def div(a,b):
 try:
   quot=a/b
 except ZeroDivisionError:
   print("Value of b can't be Zero")
   sys.exit(0)
 else:
   return quot

while True: 
 print("\n1.Addition\t\t2.Subtraction\n3.Multiplication\t4.Division\n5.Exit")
 ch=int(input("Enter the operation:"))
 if ch==1:
  a=float(input("Enter value for a:"))
  b=float(input("Enter value for b:"))
  sum=add(a,b)
  print(f"{a}+{b}={sum}")
 
 elif ch==2:
  a=float(input("Enter value for a:"))
  b=float(input("Enter value for b:"))
  diff=sub(a,b)
  print(f"{a}-{b}={diff}")
  
 elif ch==3:
  a=float(input("Enter value for a:"))
  b=float(input("Enter value for b:"))
  product=mult(a,b)
  print(f"{a}*{b}={product}")
  
 elif ch==4:
  a=float(input("Enter value for a:"))
  b=float(input("Enter value for b:"))
  quotient=div(a,b)
  print(f"{a}/{b}={quotient}")
  
 elif ch==5:
  break
  
 else:
  print("Invalid Operation Input")