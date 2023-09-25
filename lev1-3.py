'''
3. Create a python function that takes 2 numbers x, y and prints the multiplication
table from x to y

'''


def multiplicationTable(x,y):
    mul_list=[]
    for i in range(x ,y):
        mul_list.append(x*i)

    print("multiplication table is: " ,mul_list)






if __name__ =='__main__':
    x =int(input('enter first number'))
    y =int(input('enter secont number'))
    multiplicationTable(x,y)