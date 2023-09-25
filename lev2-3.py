'''
3. Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional
programming]

'''

def startWith(names ,nl=True ,lc =True , fp=True):
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
            if i.startswith('t'):
                newlist.append(i)
        print("normal list is : ",newlist)

    #list comprehension
    if lc:
        lc = [i for i in names if i.startswith('t')]
        print("list comprehension is : ",lc)
    #functional programing
    if fp:
        fp = filter(lambda x : x.startswith('t'),names)
        print("functional programming is :",list(fp ))

if __name__ == '__main__':

    Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha','tito']
    startWith(names=Names)