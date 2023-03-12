def encrypt(text,key):
    ans = ""
    for i in range(len(text)): # iterate over the given text
        ch = text[i]
        if ch==" " or not ch.isalpha(): # check if space or mark then simply add it
            ans+=ch
        elif (ch.isupper()): # check if a character is uppercase then encrypt it accordingly 
            ans += chr((ord(ch) + key-65) % 26 + 65) #A in ASCII is 65
        else: # check if a character is lowercase then encrypt it accordingly
            ans += chr((ord(ch) + key-97) % 26 + 97) #a in ASCII is 97
    return ans

def decrypt(text,key):
    ans = ""
    for i in range(len(text)): # iterate over the given text

        ch = text[i]
        if ch==" " or not ch.isalpha(): # check if space or mark then simply add it
            ans+=ch
        elif (ch.isupper()): # check if a character is uppercase then encrypt it accordingly 
            ans += chr((ord(ch) - key-65) % 26 + 65) #A in ASCII is 65
        else: # check if a character is lowercase then encrypt it accordingly
            ans += chr((ord(ch) - key-97) % 26 + 97) #a in ASCII is 97
    
    return ans

def executeBruteForceAttack(text):
    return [decrypt(text,key) for key in range(26)]

def main():

    print("\n---------------------")
    while True: #Run until ctrl+c

        while True: #Input Validation
            choice = input("Do you want to (e)ncrypt, (d)ecrypt or (b)brute-force? ")
            if(choice in ("e","d","b")):
                break

        if(choice != "b"): #encrypt/decrypt
            msg = "Please enter the key (0 to 25) to use: "
            while True: #Input Validation
                try:
                    key = int(input(msg))
                    if(key>=0 and key<=25):
                        break
                    else:
                        msg = "Not valid input. Please enter the key (0 to 25) to use: "
                except ValueError:
                    msg = "Not valid input. Please enter the key (0 to 25) to use: "
            
            #Call the appropriate function (encrypt/decrypt) with the given arguments
            text = input("Enter the message to encrypt: " if choice == "e" else "Enter the message to decrypt: ")
            print("Encrypted text: "+encrypt(text,key) if choice == "e" else "Decrypted text: "+ decrypt(text,key))

        elif(choice == "b"): #brute-force
            text = input("Please enter the encrypted msg to decrypt using brute force attack: ")
            posibilities = executeBruteForceAttack(text)

            #Results
            print("The 26 possible decrypted messages are: ")
            for i in range(len(posibilities)):
                print("#"+str(i)+": "+posibilities[i])

        print("\n---------------------")


if( __name__ == "__main__"):
    main()
