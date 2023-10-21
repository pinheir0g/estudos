#!/usr/bin/env python3

"""Caesar Encryption

This program receives a message and encrypts it using the Caesar cipher.

How to use:
    Run the program with:
        python3 cryptography_caesar.py

    Type in any message.

Returns the encrypted message.
"""

from string import ascii_uppercase 

characters = list(ascii_uppercase)

message = input('Message: ').upper()


encryption = "" 

for l in message: 
    i = ord(l)-65 
    if l in characters: 
        encryption += characters[(i+3)%26]
    else: 
        l

print(f'Mensagem criptografada: {encryption}')
