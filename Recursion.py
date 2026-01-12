def add_1(num):

    if(num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_1(total)

my_newtotal = add_1(0)
print(my_newtotal)
# for i in range(1,11):
#     print(i)