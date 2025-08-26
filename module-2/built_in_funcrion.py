from function import sum as total
# from function import * to import all

# numbers = (1,2,3,4,5)
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))
# print(total(10,20,30))


# #lamda is a shortcut function writing techique
def ghun(x):return x*x
nun = lambda x:x**x
# print("multiple :",ghun(3))
# print("power :",nun(3))

nums = [1, 2, 3]
print(list(map(ghun,nums)))
print(list(map(nun,nums)))

