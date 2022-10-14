# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Casual Coded Correspondence: The Project
#
# In this project, you will be working to code and decode various messages between you and your fictional cryptography enthusiast pen pal Vishal. You and Vishal have been exchanging letters for quite some time now and have started to provide a puzzle in each one of your letters.  Here is his most recent letter:
#
#      Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a  Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then I have my coded message,"ebiil"! Now I can send you my message and the offset and you can decode it. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer coded message that you have to decode yourself!
#     
#         xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
#     
#     This message has an offset of 10. Can you decode it?
#     
#
# #### Step 1: Decode Vishal's Message
# In the cell below, use your Python skills to decode Vishal's message and print the result. Hint: you can account for shifts that go past the end of the alphabet using the modulus operator, but I'll let you figure out how!

# +
# # %load_ext jupyter_black

import re
import string

# Creating a list of all the letters in the alphabet, punctuation, and whitespace.
alphabet = list(string.ascii_letters)
punctuation = list(string.punctuation)
whitespace = list(string.whitespace)


def decoder(message: str, offset: int) -> None:
    """
    Using the Caesar Cipher and offset to decode a message.

    Arguments:
        message -- message to decode
        offset -- offset to use for decryption
    """
    decoded_message = []

    for idx, letter in enumerate(message):
        if message[idx] in alphabet:
            # This is the formula for the Caesar Cipher.
            original_letter = alphabet[((alphabet.index(letter)) + offset) % 26]
            decoded_message.append(original_letter)
        elif message[idx] in punctuation or message[idx] in whitespace:
            decoded_message.append(message[message.index(letter)])

    # print("Coded message: ", message)
    # print("Offset: ", offset)
    print("Decoded message: ", *decoded_message, sep="")

    decoded_message.clear()


# -

decoder(
    "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!",
    10,
)


# #### Step 2: Send Vishal a Coded Message
# Great job! Now send Vishal back a message using the same offset. Your message can be anything you want! Remember, coding happens in opposite direction of decoding.

def coder(message: str, offset: int) -> None:
    """
    Using the Caesar Cipher and offset to encode a message.

    Args:
        message: message to encode
        offset: offset to use for encryption
    """
    encoded_message = []

    for idx, letter in enumerate(message):
        if message[idx] in alphabet:

            encoded_letter = alphabet[(alphabet.index(letter) - offset) % 26]
            encoded_message.append(encoded_letter)
        elif message[idx] in punctuation or message[idx] in whitespace:
            encoded_message.append(message[message.index(letter)])

    # print("Original message: ", message)
    # print("Offset: ", offset)
    print("Coded message: ", *encoded_message, sep="")

    encoded_message.clear()


coder("hello there. This message is encoded with a Caesar Cipher", 10)

# #### Step 3: Make functions for decoding and coding 
#
# Vishal sent over another reply, this time with two coded messages!
#     
#     You're getting the hang of this! Okay here are two more messages, the first one is coded just like before with  an offset of ten, and it contains the hint for decoding the second message!
#     
#     First message:
#     
#         jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
#         
#     Second message:
#     
#         bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!
#     
# Decode both of these messages. 
#
# If you haven't already, define two functions `decoder(message, offset)` and `coder(message, offset)` that can be used to quickly decode and code messages given any offset.

decoder("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10)

decoder(
    "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14
)

# #### Step 4: Solving a Caesar Cipher without knowing the shift value
#
# Awesome work! While you were working to decode his last two messages, Vishal sent over another letter! He's really been bitten by the crytpo-bug. Read it and see what interesting task he has lined up for you this time.
#
#             Hello again friend! I knew you would love the Caesar Cipher, it's a cool simple way to encrypt messages. Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
#             
#             To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of   the shift. You'll have to brute force it yourself.
#             
#             Here's the coded message:
#             
#             vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
#             
#             Good luck!
#             
# Decode Vishal's most recent message and see what it says!

for i in range(8):
    print(f"offset: {i}", end="\n")
    decoder(
        "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",
        i,
    )

# #### Step 5: The Vigenère Cipher
#
# Great work! While you were working on the brute force cracking of the cipher, Vishal sent over another letter. That guy is a letter machine!
#
#             Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
#             
#            The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
#            
#            Consider the message
#            
#                barry is the spy
#
#            If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
#            
#                dog
#                
#            Now we use the repeat the keyword over and over to generate a _keyword phrase_ that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our _keyword phrase_ is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift the each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth. Remember, we zero-index because this is Python we're talking about!
#
#                         message:       b  a  r  r  y    i  s   t  h  e   s  p  y
#                 
#                  keyword phrase:       d  o  g  d  o    g  d   o  g  d   o  g  d
#                  
#           resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5
#       
#             So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:
#             
#                 eoxum ov hnh gvb
#                 
#             As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
#             
#                 dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!
#                 
#             and the keyword to decode my message is 
#             
#                 friends
#                 
#             Because that's what we are! Good luck friend!
#            
# And there it is. Vishal has given you quite the assignment this time! Try to decode his message. It may be helpful to create a function that takes two parameters, the coded message and the keyword and then work towards a solution from there.
#
# **NOTE:** Watch out for spaces and punctuation! When there's a space or punctuation mark in the original message, there should be a space/punctuation mark in the corresponding repeated-keyword string as well! 

# +
original_message = []


class VCipher:
    # A decorator that allows the function to be called without an instance of the class.
    @staticmethod
    def generate_decoder_key(message, keyword) -> list:
        key = list(keyword)
        string = re.split(r"\w", message)

        for i in range(len(string)):
            if key[i] in alphabet:
                key.extend(key[i])
            else:
                key.extend(key[i + 1])

        return key

    @staticmethod
    def decoder_key_adjust(message, new_key) -> list:

        # Finding all the instances of the punctuation and whitespace characters in the message and returning the index of each instance using regular expressions.
        search_pattern = r"[\'!\"#$%&'()\*+,-./:;<=>?@[\]^_`{|}~\s\t\n\r\x0b\x0c]"
        punc_pos = [m.start() for m in re.finditer(search_pattern, message)]
        new_key = list(new_key)
        # Inserting the punctuation and whitespace characters into the new_key list.
        # _ used as a temporary variable.
        for _ in punc_pos:
            new_key.insert(_, message[_])

        return new_key

    @staticmethod
    def message_decoder(message, decipher) -> None:
        """
        Args:
            message (string): encrypted message received.
            decipher (list): key to use for decryption adjusted for punctuation and whitespace.
        """
        for idx, x in enumerate(message):
            if message[idx] in alphabet:
                # Finding the position of each letter before the offset
                pos = (
                    alphabet.index(message[idx]) - alphabet.index(decipher[idx])
                ) % 26
                original_message.extend(alphabet[pos])
            else:
                original_message.extend(message[idx])

    original_message.clear()

    @staticmethod
    # Function that encrypts a message using the Vigenère Cipher
    def message_encoder(message, keyword) -> list:
        encrypted_message = []
        for idx, x in enumerate(message):
            if message[idx] in alphabet:
                offset = (
                    alphabet.index(message[idx]) + alphabet.index(keyword[idx])
                ) % 26
                encrypted_message.extend(alphabet[offset])
            else:
                encrypted_message.extend(message[idx])
        return encrypted_message


# +
decryption_keyword = "friends"
received_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"

adjusted_keyword = VCipher.generate_decoder_key(received_message, decryption_keyword)
decipher_key = VCipher.decoder_key_adjust(received_message, adjusted_keyword)
VCipher.message_decoder(received_message, decipher_key)

print("Decoded message: ", *original_message, sep="")
# -

# #### Step 6: Send a message with the  Vigenère Cipher
# Great work decoding the message. For your final task, write a function that can encode a message using a given keyword and write out a message to send to Vishal!
#
# *As a bonus, try calling your decoder function on the result of your encryption function. You should get the original message back!*

# +
encryption_keyword = "hello"
decrypted_message = "This is a message sent using the Vigenère Cipher."

adjusted_keyword = VCipher.generate_decoder_key(decrypted_message, encryption_keyword)
cipher = VCipher.decoder_key_adjust(decrypted_message, adjusted_keyword)
encoded_message = VCipher.message_encoder(decrypted_message, cipher)

# print("Cipher: ", *cipher, sep="")
print("Encoded message: ", *encoded_message, sep="")
# -

# #### Conclusion
# Over the course of this project you've learned about two different cipher methods and have used your Python skills to code and decode messages. There are all types of other facinating ciphers out there to explore, and Python is the perfect language to implement them with, so go exploring! 
