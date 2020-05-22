letter_frequency = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

ETAOIN_list = []

for i in range(len(ETAOIN)):
    ETAOIN_list.append(ETAOIN[i])
# print(ETAOIN_list)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = "LIVITCSWPIYVEWHEVSRIQMXLEYVEOIEWHRXEXIPFEMVEWHKVSTYLXZIXLIKIIXPIJVSZEYPERRGERIMWQLMGLMXQERIWGPSRIHMXQEREKIETXMJTPRGEVEKEITREWHEXXLEXXMZITWAWSQWXSWEXTVEPMRXRSJGSTVRIEYVIEXCVMUIMWERGMIWXMJMGCSMWXSJOMIQXLIVIQIVIXQSVSTWHKPEGARCSXRWIEVSWIIBXVIZMXFSJXLIKEGAEWHEPSWYSWIWIEVXLISXLIVXLIRGEPIRQIVIIBGIIHMWYPFLEVHEWHYPSRRFQMXLEPPXLIECCIEVEWGISJKTVWMRLIHYSPHXLIQIMYLXSJXLIMWRIGXQEROIVFVIZEVAEKPIEWHXEAMWYEPPXLMWYRMWXSGSWRMHIVEXMSWMGSTPHLEVHPFKPEZINTCMXIVJSVLMRSCMWMSWVIRCIGXMWYMX"

def Frequency_Analysis(text):
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in text.upper():
        if letter in LETTERS:
            letter_count[letter]+=1
    
    #sort the dictionary from smallest to largest
    letter_count = sorted((value,key) for (key,value) in letter_count.items())
    #reverse the list to start from largest value
    letter_count.reverse()

    return letter_count

# print(Frequency_Analysis(text))
# output = Frequency_Analysis(text)

# Map the decrpytion key according to the frequency
def map_frequency(frequency_letters):
    decryption_key = []
    for letters in range(len(frequency_letters)):
        decryption_key.append(frequency_letters[letters][1])
    
    return decryption_key

# print((map_frequency(Frequency_Analysis(text))))

def decrypt(text):
    decryption_key = map_frequency(Frequency_Analysis(text))

    # Convert the ETAOIN list and decryption key into a dictionary
    dictionary = dict(zip(decryption_key,ETAOIN_list))
    print('Key Dictionary:','\n',dictionary)
    # print("Text before", text)


    translated_text = [dictionary[letter] for letter in text]

    #list to string
    translated_text = ''.join(translated_text)
    # translated characters shown in lower case
    translated_text = translated_text.lower()

    # print("Text after", text)

    return translated_text

decrypted_text = decrypt(text)

original_text = "hereuponlegrandarosewithagraveandstatelyairandbroughtmethebeetlefromaglasscaseinwhichitwasencloseditwasabeautifulscarabaeusandatthattimeunknowntonaturalistsofcourseagreatprizeinascientificpointofviewthereweretworoundblackspotsnearoneextremityofthebackandalongoneneartheotherthescaleswereexceedinglyhardandglossywithalltheappearanceofburnishedgoldtheweightoftheinsectwasveryremarkableandtakingallthingsintoconsiderationicouldhardlyblamejupiterforhisopinionrespectingit"

length_of_text = len(original_text)
similarity_score = 0

for i in range(length_of_text):
    if decrypted_text[i] == original_text[i]:
        similarity_score += 1

percentage_similarity = similarity_score/length_of_text
print('Similarity Percentage:','\n',percentage_similarity)

