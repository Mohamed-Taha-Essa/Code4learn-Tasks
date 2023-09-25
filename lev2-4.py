'''
4. Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional
programming]
'''
def contain2a(names ,nl=True ,lc =True , fp=True):
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
            if i.count('a')>=2:
                newlist.append(i)
        print("normal list is : ",newlist)

    #list comprehension
    if lc:
        lc = [i for i in names if i.count('a')>=2]
        print("list comprehension is : ",lc)
    #functional programing
    if fp:
        fp = filter(lambda x : x.count('a')>=2,names)
        print("functional programming is :",list(fp ))

if __name__ == '__main__':

    Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha','tito']
    contain2a(names=Names)
