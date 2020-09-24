# Trnasposition Cipher Decryption


import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptedMessage(myKey, myMessage)

    #Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message:
    print(plaintext + '|')
    
    pyperclip.copy(plaintext)

def decryptedMessage(key, message):
    # The transposition decrypted will simulate the "columns" and 
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First , we need to calculate a few values.

    # The number of "columns" in our transposition grid:

    numOfColumns = int(math.ceil(len(message) / float(key)))

    #Number of "rows" in a grid
    numOfRows = key

    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # The number of "rows" in our grid:

    # Each string in plaintext represents a column in the grid:
    plaintext = [''] * numOfColumns
    #The column and row variables point to where in the grid the next
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to the next column
 
        # If there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row:
        if (column == numOfColumns) or (column ==numOfColumns -1 and
          row >= numOfRows  - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ =='__main__':
    main()
