#Transposition Cipher Encrypt/Decrypt File

import  time, os, sys, trnsp_cipher,tnsp_decrypt

def main():
    inputFilename = 'frankeinstein.txt'
    outputFilename = 'frankeinstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'.

    # If the input file does not exist, the program terminates early:
    if os.path.exists(outputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    #If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    #Read in the message from input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long the encryption/decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = trnsp_cipher.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated =tnsp_decrypt.decryptedMessage(myKey, content)
    totaltime =round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totaltime))

    #Write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s. ' % (myMode.title(), outputFilename))


if __name__ == '__main__':
    main()