'''
5. Print a list contains the len of each word in the list using
[normal list - list comprehension -
functional programming]
'''
def lenWord(names ,nl=True ,lc =True , fp=True):
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
            newlist.append(len(i))
        print("normal list is : ",newlist)

    #list comprehension
    if lc:
        lc = [len(i) for i in names ]
        print("list comprehension is : ",lc)
    #functional programing
    if fp:
        fp = map(lambda x :len(x),names)
        print("functional programming is :",list(fp ))

if __name__ == '__main__':

    Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha','tito']
    lenWord(names=Names)
