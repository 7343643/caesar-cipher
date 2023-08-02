#opens a file called text.txt and if there is not one makes one and opens it
text = open("text.txt", "w")
#asks the user to input the text they want to encrypt or decrypt and writes the the response to the text.txt file
text.write(input("please input the text you want to be encrypt/decrypted "))
#closes the text.txt file
text.close