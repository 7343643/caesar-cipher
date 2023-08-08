#imports the random module
import random
#generates a random number from 1-25 and assigns it to the key variable
key = (random.randrange(1,26))

print(key)

shift = key - key * 2
print(shift)
print(key)