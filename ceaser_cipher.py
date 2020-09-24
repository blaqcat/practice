
import pyperclip

message = 'This is my secret message'

key = 13

mode = 'encrypt'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''


for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
         #Perform encryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex  - key

         #Handle Wraparound  if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
           trandlatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

print(translated)
pyperclip.copy(translated)

