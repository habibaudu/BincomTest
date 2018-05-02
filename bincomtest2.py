
'''
  Name : Habib Audu
  Bincom Test Answer 7
  email: auduhabib1990@gmail.com
'''
# 7.	BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.

def recur_search(list1, item):
    if len(list1) == 0:
        return 'Not found'
    else:
        mid = len(list1)//2
        if (item == list1[mid]):
            return 'Found'
        else:
            if item > list1[mid]:
                return recur_search(list1[mid+1:],item)
            else:
                return recur_search(list1[:mid],item)

list1 = [1,2,4,6,8,10,12,14]
item = int(input("enter ur number : "))
result = recur_search(list1,item)
	
print("Number was "+result+" in the List")





