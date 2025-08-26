# #list can have duplicate and indexed
bag=[0,1,2,3,4,5,6,7,8,9,10]

# # #access list item
# for fruit in bag:
#     print(fruit,end=" ")

# # #list length
# print("\n",len(bag))
# print("\n")

# #access individual list item
# print(bag[-1]) #3
# print(bag[-2]) #2
# print(bag[-3]) #1
# print(bag[-4]) #0

# #print list in range same as string
# print(bag[0:3])
# print(bag[:3])
# print(bag[1:])
# print(bag[-11:-5])

# #check if a item exist in a list
# # if "mangoo" in bag:
# #     print("yes")
# # else:
# #     print("No")

# bag[0:]=["white","black"]
# print(bag)



numbers=[2,43,62,32,52,8,6,11,84]
print(numbers[:])
print(numbers[0:9:1])
print(numbers[::1])
print(numbers[::-1])
print(numbers[8:0:-1])
print(numbers[0:9:2])
print(numbers[0:9:3])

word = "PYTHON"
print(word[::-1])   # reverse whole string → "NOHTYP"
print(word[::-2])   # reverse whole string → "NOHTYP"
print(word[-2:-5:-1]) # from index 4 down to index 2 → "OHT"