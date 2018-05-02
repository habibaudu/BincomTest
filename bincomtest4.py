
'''
  Name : Habib Audu
  Bincom Test Answer 9
  email: auduhabib1990@gmail.com
'''
# 9.	Write a program to sum the first 50 fibonacci sequence
def fibo(num):
    a=0
    b=1
    f=1
    sum2=0
    for i in range(num):
   
          sum2 +=f
          f = a+b
          a=b
          b=f
         

    print(sum2)

fibo(50)