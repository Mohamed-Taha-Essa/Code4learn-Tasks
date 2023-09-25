'''
. Create a python function that takes 2 numbers x,y and prints all the numbers between 1
 and 100 than can
be divided on x,y

'''

def dividedOnXy(x, y):
    numbers_can_divided_on_xy=[]
    for i in range(1,100):

        if i %x ==0 and i %y ==0:
            numbers_can_divided_on_xy.append(i)


    print("all numbers is : ", numbers_can_divided_on_xy)









if __name__ =='__main__':
    x =int(input('enter first number'))
    y =int(input('enter secont number'))
    dividedOnXy(x,y)