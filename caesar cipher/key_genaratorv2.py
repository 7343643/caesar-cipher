def keygen():
    #imports the random module
    import random
    global key
    global shift
    #generates a random number from 1-25 and assigns it to the key variable
    key = (random.randrange(1,26))

    #makes a variable called shift and makes it equal to key minus key times two
    shift = key - key * 2
    
    



