def hello():#defining functon
    print("hello world!".title())

hello()

# def sum(num1, num2):#parameters do not change(placeholder)
#     print(num1 + num2)

# sum(2, 3)#argumrnt can change with every function call
# sum(4, 5)
# sum(100, 3)
# #Shows reusability

#passing default value in case value not provided
def sum(num1=0, num2=0):#parameters do not change(placeholder)
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(1, 2)
print(total)

def multi_items(*args):#* makes date inside a function tuple
    print(args)
    print(type(args))

multi_items("Dave","John","Sara")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave",last = "Gray")
