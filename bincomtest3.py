
'''
  Name : Habib Audu
  Bincom Test Answer 8
  email: auduhabib1990@gmail.com
'''
# 8.	Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
import random
n = 4
binary1 = []
for i in range(10):
    ran = random.randint(1,20) #generates random numbers from 1 -20
    b = bin(ran)[2:].zfill(n)  # generate their binari forms and fills the first two digit with zeros
    binary1.append(b)
print (binary1)
decimal = 0
decimal1 = [] 
for digit in binary1:
    decimal = int(digit,2)  # converts to decimal 
    decimal1.append(decimal) 

print(decimal1)



    



   

