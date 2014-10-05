#
#  Find words in a word list that contain all the vowels in alphabetical order, non-repeated, where vowels are defined as A E I O U Y.
#


def check_words(file_name):
    vowels  = {'a','e','i','o','u','y'}
    words   = open(file_name).readlines()
    for w in words:
        w = w.rstrip()
        if(vowels <= set(w)):
            sorted_set  = []
            for c in w:
                if c in sorted_set:
                    break
                if c in vowels:
                    sorted_set.append(c)
            else:
                if sorted(sorted_set) == sorted_set:
                    cnt += 1
                    print w + " contained all vowels exactly once in alphabetical order.."

if __name__ == '__main__':
    file = "DC122e_WordsWithOrderedVowels.txt"
    check_words(file)