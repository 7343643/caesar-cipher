#makes a function called key asker
def key_asker(response):
    #makes the shift variable global
    global shift
    #makes shift equal zero
    shift = 0
    #checks if the user is decrypting 
    if response == "decrypt":
        #code loops until shift is more than zero and a whole number
        while shift <= 0:
            #asks the user to input their key and stores the awnser as a variable called shift
            shift = input("please input your key ")
            try:
                shift = int(shift)
                if shift < 1:
                    print("your key should be atleast 1")
            except:
                print("your key should be a whole number not a letter or a decimal and should be at least 1")
    if response == "encrypt":
        while shift <= 0:
            shift = input("please input your key ")
            try:
                shift = int(shift)
                if shift < 1:
                    print("your key should be atleast 1")
            except:
                print("your key should be a whole number not a letter or a decimal and should be at least 1")
        shift = shift - shift * 2