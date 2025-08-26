num = [4,45,3,7,8,24,11,43,6,23]
odd = []
for x in num :
    if x % 2 == 1 :
       odd.append(x) 
# odd.sort()
print(odd)
print(list(filter(lambda x : x % 2 == 1, num)))