#imports the text asker
import text_askerv4
#imports the shift variable from the text asker
from text_askerv4 import shift
#attempts to import the key variable from the text asker
try:
    from text_askerv4 import key
    print(key)
#if the key variable is not present the program continues without it
except:
    pass
print(shift)
from text_askerv4 import message
#imports the caesar cipher
import cipherv2
cipherv2.cipher(shift,message)
from cipherv2 import result
#prints the encrypted/decrypted text
print(result)