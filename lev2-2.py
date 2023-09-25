'''
2. Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional
programming]

'''


def containsa(names ,nl=False ,lc =False , fp=True):
    '''

    :param names: for list of string names
    :param nl: stand for normal list
    :param lc: stand for list comprehension
    :param fp: stand for functional programming
    '''
    #normal list
    if nl:
        newlist=[]
        for i in names:
            if 'a' in i :
                newlist.append(i)
        print("normal list is : ",newlist)

    #list comprehension
    if lc:
        lc = [i for i in names if 'a'in i]
        print("list comprehension is : ",lc)
    #functional programing
    if fp:
        fplist = filter(lambda x : 'a' in x ,names)
        print(list(fplist))

if __name__ == '__main__':

    Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha','tito']
    containsa(names=Names)