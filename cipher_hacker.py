#Ceaser Copher Hacker

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz1234567890 !?.'

#Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to remember to set translated to blank string
    # So that the previous iteration value for translated is cleared:
    translated = ''
    # The rest of the program is almost the same as the Ceaser program

    #Loop throught each symbol in message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key


            #Handle the wrapparound
            if translatedIndex < 0:
                transltedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrpted symbol:
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

     # Display ever possible decryption\
    print('Key #%s: %s' % (key, translated))
