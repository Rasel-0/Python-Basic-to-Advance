#list can have duplicate and indexed
bag=["mango","banana","grapes","orange"]

#access list item
for fruit in bag:
    print(fruit,end=" ")

#list length
# print("\n",len(bag))
print("\n")

#access individual list item
# print(bag[-1]) #3
# print(bag[-2]) #2
# print(bag[-3]) #1
# print(bag[-4]) #0

#print list in range same as string
# print(bag[0:2])
# print(bag[:2])
# print(bag[1:])
# print(bag[-4:-1])

#check if a item exist in a list
# if "mangoo" in bag:
#     print("yes")
# else:
#     print("No")

bag[0:]=["white","black"]
print(bag)