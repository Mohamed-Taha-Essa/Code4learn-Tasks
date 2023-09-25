'''
. Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd
and even numbers in
the x,y range

'''
def oddRange(x ,y ):
    oddlist=[]
    evenlist =[]

    for i in range(x,y):
        if i %2 == 0:
            evenlist.append(i)
        elif i %2 !=0:
            oddlist.append(i)

    print("even list" ,evenlist)
    print("odd list" ,oddlist)










if __name__ =='__main__':
    x =int(input('enter first number'))
    y =int(input('enter secont number'))
    oddRange(x,y)