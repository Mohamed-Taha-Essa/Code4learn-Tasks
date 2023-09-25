'''
4. Create a function that takes a sentence and prints the sentence without
duplicated words

'''


'''
First, we have to split the string using split() method to get the words, 
then using the fromkeys() we have created a dictionary and printed the keys in 
that dictionary as a string using the join() method.
'''
def deleltDuplicatedWords(sentence):
    # remove duplicate words from a sentence
    # using fromkeys()
    # print(sentence.split())
    # print(dict.fromkeys(sentence.split()))
    print(' '.join(dict.fromkeys(sentence.split())))





if __name__ =='__main__':
    sent = "my names is is is is taha taha taha"
    deleltDuplicatedWords(sent)