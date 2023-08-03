#opens a file called text.txt and if there is not one makes one and opens it
text = open("text.txt", "w")
#asks the user to input the text they want to encrypt or decrypt and writes the the response to the text.txt file in lowercase
text.write(input("please input the text you want to be encrypt/decrypted ").lower())
#closes the text.txt file
text.close

#prints nothing which creates a blank line in the output
print("")
#makes a variable called decrypt which contains the word decrypt
decrypt = ("decrypt")
#makes a variable called response which is empty
response = ("")
#makes a variable called encrypt which contains the word encrypt
encrypt = ("encrypt")
#makes a loop that will ask the user if they want to encrypt or decrypt and will only stop when a either encrypt or decrypt
while response != encrypt or decrypt:
    #ask the user if they want to encrypt or decrypt and assings the awnser in lowercase to a variable called response
    response = input("do you want to encrypt or decrypt the text you inputted ").lower()
    #prints nothing which causes a gap in between the previous and next output
    print("")
    #checks if the response is decrypt and ends the loop if it is
    if response == decrypt:
        break
    #checks if the response is encrypt and ends the loop if it is
    if response == encrypt:
        break
#checks if the users input was encrypt and starts the key generator if it was
if response == encrypt:
    #tells the user that the key generator is starting
    print("starting key generator")
    #imports the key generator
    import key_genarator
#checks if the users input was decrypt and starts the key asker if it was
else:
    if response == decrypt:
        #imports the key generator
        import key_asker
    #prints an error if the user inputted something other than encrypt or decrypt, but instead of looping until a valid input the program broke the loop
    else:
        print("error_1")