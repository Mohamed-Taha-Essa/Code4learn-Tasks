"""
8. Create a function that takes x,y and prints all the number that can be divide by y
from x to 100


"""
def divideByY(x, y):
    divide_by_y = []
    for i in range(x,100):
        if i % y == 0:
            divide_by_y.append(i)
        else:continue
    print(divide_by_y)




if __name__ == '__main__':
    x = int(input('enter x '))
    y = int(input('enter y '))
    divideByY(x ,y)