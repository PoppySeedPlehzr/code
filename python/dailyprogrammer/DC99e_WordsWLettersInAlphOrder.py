def count_alphabetized_words():
    words = open('DC99e_WordsWLettersInAlphOrder_lib.txt','r').readlines()
    cnt = 0
    for tmp in words:
        #word = tmp[:-2]
        word = tmp[:-1]
        #sorted_word = ''.join(sorted([char for char in word]))
        sorted_word = ''.join(sorted(word))
        if(word == sorted_word):
            #print word + ' matched ' + sorted_word
            cnt += 1
    print cnt

if __name__ == '__main__':
    count_alphabetized_words()
