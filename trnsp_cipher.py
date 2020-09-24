import pyperclip

def main():
    myMessage  = 'common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    #Print the encypted string in ciphertext to the screen, with
    # a | ("pipe" character) after  it in case there are spaces at
    # the end of the encypted message:
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    #Each string in the cipher text represents a column in  the grid:
    ciphertext = ['']*key

    # Loop through each column in the cipher text
    for column in range(key):
        currentIndex = column

        #Keep  looking until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the cipher text list
            ciphertext[column] += message[currentIndex]

            # Now move currentIndex over 
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
