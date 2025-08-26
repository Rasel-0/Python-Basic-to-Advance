#numbers with default perameter
def sum(num1,num2,num3=0):
    return num1+num2+num3
total = sum(10,20,30)
print(total)

#normally passing arguments has default order but custom order can be set by key argument
def kargs(size, tuple):
    print(size)
    print(tuple)
kargs(tuple=1,size=5)

#def(num,*tuple,**dictionary):
#multiple argument passing using args
def args(size, *tuple):
    print(size)
    print(tuple)
    for value in tuple:
        print(value)
args(1,2,3,4,5)

def dic_args(size, **dic):
    print(size)
    print(dic)
    print(dic["name"])
dic_args(1,name="rasel",age=24,roll="devOps engineer")

def operation( n1,n2,n3):
    add = n1+n2+n3
    mul = n1*n2*n3
    #return add , mul tuple
    # return [add , mul] list 
    # return {add , mul} object or dictionary
result = operation(2,3,5)
print(result) #tuple
