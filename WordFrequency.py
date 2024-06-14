def main():
    word_freq = count_word_frequencies()
    display_word_frequencies(word_freq)

#count word frequencies
def count_word_frequencies():
    
    #create empty dictionary
    word_freq = {}

    #open file and covernteverything to lower case
    file = open('sometext-1.txt','r')
    text = file.read().lower()
    file.close()

    #remove punctuation
    punctuation = '''!.?'"'''
    for char in punctuation:
        text = text.replace(char, '')
    

    #Split text into words
    words = text.split()

    #Count frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

#display word frequencies
def display_word_frequencies(word_freq):
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

#call main
main()