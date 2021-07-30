#Assignment 2
#Remove Occurence Of Elements In List

items = input('To Check Operation: Remove Occurence Of Elements In A List,  Enter Few Items and Repeat Some Items in it')
list = items.split()

result = []   
for i in list:
      if i not in result:
  	     result.append(i)
print(result)