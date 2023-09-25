

'''
7. Create a function takes a sentence and a word and prints how many time the word
used in the sentence

'''

def countWord(sentence ,word):
    count = sentence.count(word)
    print(f" {word} comes {count} time ")



if __name__ == '__main__':
    sent = "my names is is is is Mohamed Abdallah Essa"
    word ='Mohamed'
    countWord(sent ,word)