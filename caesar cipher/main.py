import text_askerv4
from text_askerv4 import shift
try:
    from text_askerv4 import key
    print(key)
except:
    pass
print(shift)
from text_askerv4 import message

import cipherv2
cipherv2.cipher(shift,message)
from cipherv2 import result
print(result)