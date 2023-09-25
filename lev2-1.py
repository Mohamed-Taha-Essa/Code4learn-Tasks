'''
1. Transform all names to uppercase using [normal list - list comprehension - functional programming]

'''


def uppercase(names ,nl=False ,lc =False , fp=True):
    '''

    :param names: for list of string names
    :param nl: stand for normal list
    :param lc: stand for list comprehension
    :param fp: stand for functional programming
    '''
    #normal list
    if nl:
        normalList =str(names)
        print("normal lisr is : ",normalList.upper())

    #list comprehension
    if lc:
        lc = [i.upper() for i in names]
        print("list comprehension is : ",lc)
    #functional programing
    if fp:
        fp =map(lambda x:x.upper() ,names)
        print(list(fp))

if __name__ == '__main__':

    Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']
    print((lambda s: s[::-1])(Names))
    uppercase(names=Names)