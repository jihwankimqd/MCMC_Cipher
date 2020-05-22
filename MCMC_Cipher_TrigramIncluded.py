import string
import math
import random
import numpy as np

# initialize the alphabet and convert it into a list
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_list = list(LETTERS)
# print(alphabet_list)

# take an input cipher and create a dictionary which maps the alphabet onto its cipher dict.
# e.g {D: I, X:J, Y: P, ...}
def cipher_dictionary(cipher):
    cipher_dict = {}
    for letter in range(len(cipher)):
        cipher_dict[alphabet_list[letter]] = cipher[letter]
    return cipher_dict

# apply cipher onto the input text to output the encrypted text
def encrypt_text(text,cipher):
    #create the cipher dictionary which maps the alphabet to its substitution letters
    cipher_dict = cipher_dictionary(cipher)
    #convert string format text into list format
    text = list(text)
    #initialize the encrpyted text string to append the new text
    encrypted_text = []
    for letter in text:
        if letter.upper() in cipher_dict:
            encrypted_text.append(cipher_dict[letter.upper()])
        else:
            encrypted_text.append(' ')
    # the output will be in list, so to make it easier to view, convert it into a string
    encrypted_text = ''.join(encrypted_text)
    return encrypted_text


# Mine text data from a sample text, and create a dictionary to map unigrams and bigrams and their frequencies.
# Will be used as a score in the MCMC method.
def text_frequency_analysis(text):
    letters_frequency = {}
    # to open a file and read it line by line, use the 'with open' block 
    with open(text) as textfile:
        for line in textfile:
            # returns a list of individual characters of a single line. Using .strip() clears the '\n' so it should be used to clean the data
            letter_data = list(line.strip())
            # print(letter_data)
            for i in range(len(letter_data)-2):
                unigram = letter_data[i].upper()
                bigram = letter_data[i+1].upper()
                trigram = letter_data[i+2].upper()
                # if its not an empty space and not found in alphabet, it must be garbage words such as '\ufeff' which can be found in text formatting and introduction, but not in the actual text
                if unigram != ' ' and unigram not in alphabet_list:
                    # replace these garbage words with ' '
                    unigram = ' '
                #bigram referring to letter after the current letter
                if bigram != ' ' and bigram not in alphabet_list:
                    bigram = ' '
                #trigram referring to letter two letters after the current letter
                if trigram != ' ' and trigram not in alphabet_list:
                    trigram = ' '
                combined_letter = unigram+bigram+trigram
                # combined_letter = unigram+bigram

                # if letter found in dictionary, add 1 to its count
                if combined_letter in letters_frequency:
                    letters_frequency[combined_letter] += 1
                # if first time encountering this letter, add it to the dictionary.
                else:
                    letters_frequency[combined_letter] = 1
    return letters_frequency


    

# Comment/uncomment these sections to change reference texts
# this will serve as a score metric to test the scores of individual trials

# score_metric = text_frequency_analysis('war_and_peace_.txt')
score_metric = text_frequency_analysis('alice_in_wonderland_.txt')


# Initially the above text_frequency_analysis function was going to be used to analyse the cipher
# But, the input datatype is different so a mirror function specific for the input cipher text datatype had been created.
def text_frequency_analysis_oncipher(text):
    letters_frequency = {}
    # to open a file and read it line by line, use the 'with open' block 
            # returns a list of individual characters of a single line. Using .strip() clears the '\n' so it should be used to clean the data
    letter_data = list(text)
    # print(letter_data)
    for i in range(len(letter_data)-2):
        unigram = letter_data[i].upper()
        bigram = letter_data[i+1].upper()
        trigram = letter_data[i+2].upper()
        # if its not an empty space and not found in alphabet, it must be garbage words such as '\ufeff' which can be found in text formatting and introduction, but not in the actual text
        if unigram != ' ' and unigram not in alphabet_list:
            # replace these garbage words with ' '
            unigram = ' '
        #bigram referring to letter after the current letter
        if bigram != ' ' and bigram not in alphabet_list:
            bigram = ' '
        #trigram referring to letter two letters after the current letter
        if trigram != ' ' and trigram not in alphabet_list:
            trigram = ' '
        combined_letter = unigram+bigram+trigram
        # combined_letter = unigram+bigram

        # if letter found in dictionary, add 1 to its count
        if combined_letter in letters_frequency:
            letters_frequency[combined_letter] += 1
        # if first time encountering this letter, add it to the dictionary.
        else:
            letters_frequency[combined_letter] = 1

    return letters_frequency

# Instead of using the final decryption key, the best scoring key should be used. Because for example,
# 'OLIVER' may become 'OBIVER' as iterations increase, which is not accurate. Therefore, a score for each
# cipher is needed, and the best scoring cipher should be returned.

def cipher_score(text, cipher):
    working_text = encrypt_text(text,cipher)
    cipher_frequency = text_frequency_analysis_oncipher(working_text)
    trial_score = 0
    # loop through the dictionary of the cipher_frequency dict
    # if the key in cipehr_frequency dict appears in score_metric, add score.
    # after testing simple summation tries for the score, it does not converge. Therefore, new method is neeeded.
    # referencing Rosenthal, "This function can be thought of as multiplying, for each consecutive pair of letters in the decrypted
    # text, the number of times that pair occurred in the reference text."
    for key, value in cipher_frequency.items():
        if key in score_metric:
            trial_score += math.log(score_metric[key]**value)
    return trial_score

# current_cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(generate_cipher(current_cipher))

def generate_random_cipher(cipher):
    # random shuffle on the cipher to propose a new cipher did not yield good results and most importantly
    # it doesn't converge. Therefore a new method is needed.
    # cipher = list(cipher)
    # random.shuffle(cipher)
    # return ''.join(cipher)

    # cipher = ''.join(random.sample(cipher,len(cipher)))
    # return cipher

    # thinking on the opposite end of the extreme, if shuffling the whole list doesnt converge, 
    # tried shuffling only 2 letters, and it converged. Very surprising.
    # upon thinking about the reason, it may be because shuffling the entire list into a new form
    # discards the previous cipher despite how high its score may be. It is same as nearly finishing
    # the process, and starting over again. Of course this won't converge. Therefore next generated cipher
    # should be based on the previous cipher, which is the best when the shuffle is at its minimum.
    # the lack of randomness can be compensated by the number of trials. It is expected to be guranteed to 
    # converge in this way.
    random_number1 = random.randint(0,len(list(cipher))-1)
    random_number2 = random.randint(0,len(list(cipher))-1)

    cipher = list(cipher)
    temp = cipher[random_number1]
    cipher[random_number1] = cipher[random_number2]
    cipher[random_number2] = temp
    cipher = ''.join(cipher)
    return cipher

def MCMC_cipher(iterations, text):
    current_cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    best_state = ''
    trial_score = 0
    for i in range(iterations):
        new_cipher = generate_random_cipher(current_cipher)
        current_cipher_score = cipher_score(text, current_cipher)
        next_cipher_score = cipher_score(text,new_cipher)
        # referencing Lecture notes 11, pg 5/16, the acceptance ratio,
        acceptance_probability = min(1, math.exp(next_cipher_score-current_cipher_score))
        if current_cipher_score > trial_score:
            best_state = current_cipher
        # choosing whether to accept the new cipher. Referenced from Lecture 10 example codes. FULL_MCMC.py
        if acceptance_probability >= random.uniform(0,1):
            current_cipher = new_cipher
        if i%500 == 0:
            print('Iteration ',i,':', encrypt_text(text,current_cipher)[0:99])
        final_text = encrypt_text(text,current_cipher)
    return final_text,best_state

# Function to test similarity of the decrpyted and original text
def text_similarity(original_text, decrypted_text):
    original_text = original_text.upper()
    decrypted_text = decrypted_text.upper()
    length_of_text = len(original_text)
    similarity_score = 0
    for i in range(length_of_text):
        if decrypted_text[i] == original_text[i]:
            similarity_score += 1
    return similarity_score/length_of_text

# Change the sample text by commenting/uncommenting these sections.


# Sample text from Oliver Twist
# testing_text = "As Oliver gave this first proof of the free and proper action of his lungs, \
# the patchwork coverlet which was carelessly flung over the iron bedstead, rustled; \
# the pale face of a young woman was raised feebly from the pillow; and a faint voice imperfectly \
# articulated the words, Let me see the child, and die. \
# The surgeon had been sitting with his face turned towards the fire: giving the palms of his hands a warm \
# and a rub alternately. As the young woman spoke, he rose, and advancing to the bed's head, said, with more kindness \
# than might have been expected of him: "

# Sample text from Pride and Prejudice
testing_text = "It is a truth universally acknowledged, that a single man in\
possession of a good fortune, must be in want of a wife.\
However little known the feelings or views of such a man may be\
on his first entering a neighbourhood, this truth is so well\
fixed in the minds of the surrounding families, that he is\
considered the rightful property of some one or other of their daughters."

encryption_key = "XEBPROHYAUFTIDSJLKZMWVNGQC"
cipher_text = encrypt_text(testing_text,encryption_key)
decryption_key = "ICZNBKXGMPRQTWFDYEOLJVUAHS"

print("Encrypted Text:", cipher_text)
print("\n")
final_state, best_state = MCMC_cipher(10000,cipher_text)
print('Similarity: ',text_similarity(testing_text,final_state))
print("\n")
print("Decrypted Text:",encrypt_text(cipher_text,best_state))
print("\n")
print("Decryption Key:",best_state)
print("ACTUAL DECRYPTION KEY:",decryption_key)