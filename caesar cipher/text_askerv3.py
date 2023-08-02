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
response = ("")
encrypt = ("encrypt")
while response != encrypt or decrypt:
    response = input("do you want to encrypt or decrypt the text you inputted ").lower()
    print("")
    if response == decrypt:
        break
    if response == encrypt:
        break
#checks if the users input was encrypt and starts the key generator if it was
if response == encrypt:
    #tells the user that the key generator is starting
    print("starting key generator")
    import key_generator
else:
    if response == decrypt:
        import key_asker
    else:
        print("error_1")