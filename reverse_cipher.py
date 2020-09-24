#Reverse Cipher Program

message = 'Three can keep a secret, if two of the are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    trnslated = translated + message[i]

    i = i - 1

print(translated)

