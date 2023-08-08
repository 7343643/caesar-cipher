def key_asker():
    global shift
    shift = 0
    while shift <= 0:
        shift = input("please input your key ")
        try:
            shift = int(shift)
            if shift < 1:
                print("your key should be atleast 1")
        except:
            print("your key should be a whole number not a letter or a decimal and should be at least 1")
    