'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''



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
        print("Key "+str(i)+": " ,decrypted_text)
        


encrypted_message = input("Enter the message to decrypt: ")
caesar_cipher_cracker(encrypted_message)