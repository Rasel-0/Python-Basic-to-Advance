#list as price

numbers = [12,14,63,57,35,25,95,43]

# numbers.append(20)
# #12,14,63,57,35,25,95,43,20

# numbers.extend([40,50])
# #12,14,63,57,35,25,95,43,20,40,50

# numbers.insert(0,100)
# #100,12,14,63,57,35,25,95,43,20,40,50

# #remove the first occurence of a value
# numbers.remove(12)
# #100,14,63,57,35,25,95,43,20,40,50

# numbers.pop()
# #100,14,63,57,35,25,95,43,20,40
# numbers.pop(0)
# #14,63,57,35,25,95,43,20,40

# # numbers.clear()
# #[]

# #find the index of the first occurence
# #print(numbers.index(63))
# #1 
# #print(numbers.index(2,63))
# # this search the value starting from index 2 so it is not found


# # print(numbers.count(63))
# numbers.sort()
# # # numbers.sort(reverse=True)
# numbers.reverse()
# print(numbers)

fruits = ["bananaaaa", "appleee", "cherry"]

fruits.sort(key=len)
print(fruits)

fruits.sort(key= lambda x:x[0])
print(fruits)
