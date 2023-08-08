#makes a function called cipher
def cipher(shift, message):
    #makes the result variable global
    global result
    #makes the result variable empty
    result = ""
    #makes a variable called alphabet which contains the alphabet
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