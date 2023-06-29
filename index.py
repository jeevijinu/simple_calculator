a=int(input("value1 : "))
b=int(input("value2 : "))
print("""select operation
      1.addition
      2.subtraction
      3.multiplication
      4.division quotient
      5.division remainder""")
c=int(input("enter choice : "))
if c==1:
 print(a+b)
elif c==2:
 print(a-b)
elif c==3:
 print(a*b)
elif c==4:
 print(a/b)
elif c==5:
 print(a%b)
else:
 print("value not determined")
