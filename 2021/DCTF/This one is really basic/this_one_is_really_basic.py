#!usr/bin/env python3

#import modules
import base64

#input
message = open("cipher.txt").read()

#the loop for decoding base64 till we get the flag
while True:
    try:
        message = base64.b64decode(message)
    except Exception:
        break

print(bytes.decode(message))
