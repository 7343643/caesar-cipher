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
            #trys to turn the shift variable into an intger
            try:
                shift = int(shift)
                #checks if shift is less than 1 and if it is tells the user that their key needs to be at least 1
                if shift < 1:
                    print("your key should be atleast 1")
                    shift = 0
            # if shift can not be turned into a int tell tell the user that their key needs to be a whole number not a letter and at least 1
            except:
                print("your key should be a whole number not a letter or a decimal and should be at least 1")
                #makes shift equal 0
                shift = 0
    #runs the code contained if the use is encrypting
    if response == "encrypt":
        #repeats the code contained until shift is more than 0 and a whole number
        while shift <= 0:
            #asks the user to input their key and stores the awnser in a variable called shift
            shift = input("please input your key ")
            #trys to turn the shift variable into an intger
            try:
                shift = int(shift)
                #checks if shift is less than 1 and if it is tells the user that their key needs to be at least 1
                if shift < 1:
                    print("your key should be atleast 1")            
                    shift = 0
            # if shift can not be turned into a int tell tell the user that their key needs to be a whole number not a letter and at least 1
            except:
                print("your key should be a whole number not a letter or a decimal and should be at least 1")
                #makes shift equal to zero
                shift = 0
        #turns the shift into a negative if the user is encrypting
        shift = shift - shift * 2