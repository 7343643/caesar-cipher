#makes a function called cipher
def cipher(shift, message):
    #makes the result variable global
    global result
    #makes the result variable empty
    result = ""
    #makes a variable called alphabet which contains the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #repeats the code contain for each letter inside the variable message
    for letter in message:
        #only runs the code contained if the letter is in the variable alphabet
        if letter in alphabet:
            #finds the position of the letter in the variable alphabet and assigns it to a variable called index
            index = alphabet.find(letter)
            index = (index + shift)
            if index > 25:
                while index > 25:
                    index = index - 26
            if index < -25:
                while index < -25:
                    index = index + 26
            result = result + alphabet[index]
        #if the letter is not in the alphabet the letter is added to the result without being encrypted/decrypted
        else:
            result = result + letter