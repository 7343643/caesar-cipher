#asks the user to input the text they want to encrypt or decrypt and writes the the response to the text.txt file in lowercase
message = (input("please input the text you want to be encrypt/decrypted ").lower())
#closes the text.txt file


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
    else:
        if response == encrypt:
            break
        #if the response it not encrypt tell the user to enter encrypt or decrypt
        else:
            print("please enter encrypt or decrypt")

#imports the key asker
import key_askerv2
#starts the key asker
key_askerv2.key_asker(response)
#imports the shift variable from the key asker
from key_askerv2 import shift