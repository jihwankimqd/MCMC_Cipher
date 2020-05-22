Monte Carlo Methods to Decrypt Substitution Ciphers

![Alt Text](https://github.com/jihwankimqd/MCMC_Cipher/blob/master/mcmc_run_code.gif?raw=true)

#Abstract

This project will investigate the use of Markov Chain Monte Carlo (MCMC) methods to tackle random substitution ciphers. Python and its relevant libraries will be used to implement the algorithms and visualize the results.

#Motivation

Upon first encountering the movie “The Imitation Game”, which features Alan Turing’s efforts to decode Nazi Germany’s Enigma Code during WWII, the concept of using computers to implement logic to solve problems was very fascinating. It depicted the ingenuity of Turing and the tenure in solving even the simplest ciphers. However, with the development of computers and mathematics, it became increasingly accessible to tackle such problems. Serving this as an inspiration, this project will aim to decrypt substitution ciphers using MCMC.

#Introduction and Background

Cryptography is the study of algorithms to encrypt and decrypt messages between senders and receivers. MCMC method is a class of algorithms for sampling from a probability distribution. In Cryptography, the original text is referred to as the plain text, and the encrypted text is referred to as the cipher text. The algorithms to perform these encryption and decryption are referred to as ciphers. Ciphers are classified in two categories: classical ciphers and modern ciphers. Classical ciphers refer to simpler ciphers such as substitution ciphers and transposition ciphers that operate at the byte level. Modern ciphers are much more complex such as the RSA and the DES algorithm, which are much more secure and used in modern technologies.

#Methodology

Learning from the previous section, a larger text is needed to mine the frequency of the unigrams and bigrams (and possibly trigrams) which appear in the text. Project Gutenberg[2] offered free to use and distribute English classics in .txt format, which was precisely what was needed in this method. Initially, War and Peace, and Oliver Twist had been used.

Multiple functions were needed to execute the program:
1)	The encrypt_text function applies cipher onto the input text to output the encrypted text.

2)	The text_frequency_analysis function mines text data from a sample long text (English Classics in txt format) and creates a dictionary to map unigrams and bigrams and their frequencies.

3)	The text_frequency_analysis_oncipher is used to mirror the text_frequency_analysis function but is customized for shorter texts of string datatype. Initially, the same function was going to be used, but the different datatypes and methodologies to read them were different, and therefore a new function as created.

4)	The cipher_score function returns the score of the trial cipher.

5)	The generate_random_cipher function generates random ciphers to test and score.

6)	The MCMC_cipher is the key part where all the helper functions come together to implement the MCMC method.

7)	The text_similarity function compared the similarity of the decrypted text to the original text, and returned the percentage similarity.

#Results

Upon executing the code, the results converged well and the similarity was very high for Oliver Twist’s sample text with War and Peace as the text for frequency analysis. However, the result did not always converge (although it did most of the time). If the cipher was misdirected into a bad random direction with a high score, the final cipher was entirely wrong, no matter how long the iteration. This may be improved by implementing trigram frequency analysis in the code. (Refer to mcmc_run_code.gif for the animation)

The similarity percentage did not significantly change, so this may be suggesting using unigrams and bigrams alone are sufficient. However, to test more on this, new texts were used: Alice in Wonderland and  Pride and Prejudice.
When Alice in Wonderland was used as a reference text and sample from Pride and Prejudice was used to test the code, the inclusion of trigrams showed significant improvement in accuracy. Without the frequency analysis of trigrams included as a reference, the similarity was only 70%, but with the trigrams included, without sacrificing computation time (the computation time was negligible, because both were quick), the similarity was 98%.

Therefore, it can be concluded that trigrams will generally increase the accuracy of the output, but this is dependent on the sample text and reference text. If the sample and references were relatively compatible and already accurate, using trigrams would not show much change in accuracy, but if the sample and reference text are not very compatible, trigrams improve the accuracy significantly better. This can be generalized to n-grams, but it must be balanced between the computation time and accuracy. Using very high number of n would cost a lot of computation time, but it may not always be needed because as the results show, unigrams and bigrams (and trigrams if needed) as enough to suffice for general English classic texts.
