#Declare and initialize your variables
userInput = ""
loginUser = ""

#Ask the user are you sisy or rab3awy :D ?
userInput = input("Hi :) ! Please define if u are sisy or rab3a\n").lower()

#choose the correct user for the app
if userInput in("sisy","sesy") :
    print("Hey there .. Sorry :D this application is not designed for you ...")
elif userInput in("rab3a","rab3awy") :
    print("""Nice ^_^ ! they are agda3 nas :) !
    This is "2nd way password Application Demo"
    u will have 2options the 1st one for the 1st password you choose
    the 2nd one is for the 2nd password you choose to protect your self from the bad guys
    ok .. Now please choose your 1st password which will lead to ur real device""")
    import getpass
    pswd1 = getpass.getpass("Password1: ")
    pswd2 = getpass.getpass("password2: ")

    print("""Okay.. you now choosed the first real password which will lead to ur real device\
to be """ + pswd1 + '"')
    print("""and choosed the fake password which will lead to fake data to be """ '"'+ pswd2 + '"')

    print("Let's make a small Demo ? .. You are in peace and using ur mobile please enter the peace password which is: " + pswd1)
    loginUser = getpass.getpass("Please Enter Device password \nPassword: ")
    if loginUser == pswd1 :
        print("you are using ur real device now ... (Y)")
    elif loginUser == pswd2 :
        print("this is the fake device !! don't worry about your data")
    else :
        print("wrong password")
    print("Let's make a small Demo Again ? .. You are in Danger :( please enter the tricky password which is: " + pswd2)
    loginUser = getpass.getpass("Please Enter Device password \nPassword: ")
    if loginUser == pswd1 :
        print("you are using ur real device now ... (Y)")
    elif loginUser == pswd2 :
        print("this is the fake device !! don't worry about your data")
    else :
        print("wrong password")
else:
    print("it's not 1 or 2")