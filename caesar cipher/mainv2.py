#imports the text asker
import text_askerv4
#imports the shift variable from the text asker
from text_askerv4 import shift
#imports the message from the text asker (the message the user wants to encrypt/decrypt)
from text_askerv4 import message
#imports the caesar cipher
import cipherv2
#runs the cipher
cipherv2.cipher(shift,message)
#imports the encrypted/decrypted text 
from cipherv2 import result
#prints the encrypted/decrypted text
print(result)