# %% [markdown]
# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
# encrypts letters by shifting them over by a 
# certain number of places in the alphabet. We 
# call the length of shift the key. For example, if the 
# key is 3, then A becomes D, B becomes E, C becomes 
# F, and so on. To decrypt the message, you must shift 
# the encrypted letters in the opposite direction. This 
# program lets the user encrypt and decrypt messages 
# according to this algorithm.
# 
# When you run the code, the output will look like this:
# 
# Do you want to (e)ncrypt or (d)ecrypt?
# > e
# Please enter the key (0 to 25) to use.
# > 4
# Enter the message to encrypt.
# > Meet me by the rose bushes tonight.
# QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# 
# 
# Do you want to (e)ncrypt or (d)ecrypt?
# > d
# Please enter the key (0 to 26) to use.
# > 4
# Enter the message to decrypt.
# > QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# MEET ME BY THE ROSE BUSHES TONIGHT.

###### SOLUTION #########
""" Caesar Cipher
    By Albert Andemir'irenge Gubanja
"""

#Function for encryption

def encrypt(stringToEncrypt,shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stringToEncrypt = stringToEncrypt.upper().split()
    encrypted_text = ""
    for word in stringToEncrypt:
        for letter in word:
            if letter in alphabet:
                encrypted_text += alphabet[(alphabet.index(letter) + shift) % 26]
            else:
                encrypted_text += letter
            # This is the same as the line above. If we choose to do it without the modulo operator.
            # indexLetter = alphabet.index(letter) + shift
            # if indexLetter >  25:
            #     indexLetter = indexLetter-26
            # encrypted_text += alphabet[indexLetter]
                
        encrypted_text += " "
    return encrypted_text


# Function for decryption
def decrypt(stringToDecrypt,shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stringToDecrypt = stringToDecrypt.upper().split()
    decrypted_text = ""
    for word in stringToDecrypt:
        for letter in word:
            if letter in alphabet:
                decrypted_text += alphabet[(alphabet.index(letter) - shift) % 26]
            else:
                decrypted_text += letter
        decrypted_text += " "
    return decrypted_text


#Main program
# print("Do you want to (e)ncrypt or (d)ecrypt?")
# toDo=input()
# while toDo != "e" and toDo != "d":
#     print("Please enter e or d")
#     toDo=input().lower()

# if toDo == "e":
#     print("Please enter the key (0 to 25) to use.")
#     encryptionKey = input()
#     while True:
#         try:
#             encryptionKey = int(encryptionKey)
#             if encryptionKey < 0 or encryptionKey > 25:
#                 print("Please enter a number between 0 and 25")
#                 encryptionKey = input()
#                 continue
#             break
#         except ValueError:
#             print("Please enter a number")
#             encryptionKey = input()
#         encryptionKey
#     print("Enter the message to encrypt.")
#     message = input()
#     print(encrypt(message, encryptionKey))
# else:
#     print("Please enter the key (0 to 25) to use.")
#     encryptionKey = input()
#     while True:
#         try:
#             encryptionKey = int(encryptionKey)
#             if encryptionKey < 0 or encryptionKey > 25:
#                 print("Please enter a number between 0 and 25")
#                 encryptionKey = input()
#                 continue
#             break
#         except ValueError:
#             print("Please enter a number")
#             encryptionKey = input()
#         encryptionKey
#     print("Enter the message to decrypt.")
#     message = input()
#     print(decrypt(message, encryptionKey))



#Caesar Cipher cracker

def caesar_cipher_cracker(cipher_text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = cipher_text.upper().split()
    
    for i in range(1, 27):
        decrypted_text = ""
        for word in cipher_text:
            for letter in word:
                if letter in alphabet:
                    decrypted_text += alphabet[(alphabet.index(letter) - i) % 26]
                else:
                    decrypted_text += letter
            decrypted_text += " "
        print("Round"+str(i)+": " ,decrypted_text)
        
        


caesar_cipher_cracker("HUTPUAX SUT VÈXK, P'KYVÈXK WAK BUAY BUAY VUXZKF HOKT")