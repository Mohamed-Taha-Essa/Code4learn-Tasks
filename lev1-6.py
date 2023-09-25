"""
6. Create a function that takes a sentence and word and remove the word from the sentence
"""


def removeWord(sentence ,word):
    print('new sentence is : ' ,sentence.replace(word,''))





if __name__ == '__main__':
    sent = "my names is Mohamed Abdallah Essa"
    word ='names'
    removeWord(sent ,word)