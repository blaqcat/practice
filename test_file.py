# Transposition Cipher Tsst

import random, sys, trnsp_cipher, tnsp_decrypt

def main():
    random.seed(42) # Set the random seed to static value

    for i in range(20):
        #Generate random message to tp test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) #convert the list to shuffle to s string.

        print('Test #%s: "%s..."'% (i +1, message[:50]))

        # Check all possible keys for each message
        for key in range(1, int(len(message)/2)):
            encrypted = trnsp_cipher.encryptMessage(key, message)
            decrypted = tnsp_decrypt.decryptedMessage(key, encrypted )

            # If the decryption doesn't match the original message
            # display an error message asnd quit
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

# IF test_file.py is run instead of the imported module call
# the main() function:
if __name__ == '__main__':
    main()