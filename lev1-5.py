'''
5. Create a function that takes a sentence and prints how many words in the sentence
 (do not count the
spaces)

'''
def couuntWords(sentences):
    print("number of words is :",len(sentences.split()))


if __name__ =='__main__':
    sent = "my names is is is is taha taha taha"
    couuntWords(sent)
