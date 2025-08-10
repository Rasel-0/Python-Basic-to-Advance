#numbers with default perameter
def sum(num1,num2,num3=0):
    return num1+num2

total = sum(10,20,30)
# print(total)

#multiple argument passing using args
def args(size, *tuple):
    print(size)
    print(tuple)
args(1,2,3,4,5)
