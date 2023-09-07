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
            #adds the shift to the index
            index = (index + shift)
            #runs the code contained if the variable index is more than 25
            if index > 25:
                #removes 26 from index until index is less than or equal to 25
                while index > 25:
                    index = index - 26
            #runs the code contained if the variable index is less than -25
            if index < -25:
                #adds 26 to index until index is more than or equal to -25
                while index < -25:
                    index = index + 26
            #adds the encoded letter to a variable called result
            result = result + alphabet[index]
        #if the letter is not in the alphabet the letter is added to the result without being encrypted/decrypted
        else:
            result = result + letter
    #creates a file called message.txt if one is not present and opens it
    output = open("message.txt", "w")
    #writes the encoded message to the file
    output.write(result)
    #closes the file
    output.close