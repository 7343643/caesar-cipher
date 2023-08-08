#makes a function called cipher
def cipher(shift, message):
    global result
    
    result = ""
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter)
            index = (index + shift)
            if index > 25:
                index = index - 26
            
            
            result = result + alphabet[index]
        else:
            result = result + letter