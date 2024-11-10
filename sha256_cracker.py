from pwn import * 
import sys
import hashlib

password_file = "rockyou.txt"
attempts = 0

def decode():
    global attempts
    given_hash = input("Please paste the hash you wanna crack:")
    with log.progress("starting cracking") as p:
        with open(password_file,"r", encoding='latin-1') as password_list:
            for password in password_list:
                password=password.strip("\n").encode('latin-1')
                password_hash=sha256sumhex(password)
                if password_hash == given_hash:
                    p.success(f"\r[X]Success! {password.decode('latin-1')}=={given_hash} ")
                    print(f'[X] Number of attempts = {attempts}')
                    sys.exit()
                attempts += 1
            p.failure(f"\nUnable to crack the hash after {attempts} attempts!")

def encode():
    keyword = input("Please enter the word you wanna sha256 encode:")
    keyword = keyword.strip("\n").encode('latin-1')
    hashed = sha256sumhex(keyword)
    print(f"[X] Success! {keyword} == {hashed}")
    exit()

def help():
    print(f'''>>Usage:
<{sys.argv[0]}> enc     -- to encode any keyword
<{sys.argv[0]}> dec     -- to decode any sha256 hash
<{sys.argv[0]}> help    -- to see and exit this help menu''')
    exit()

try:
    if len(sys.argv) != 2:
        print("\r")
        print(f"Invalid Number of Arguments! >>Usage: <{sys.argv[0]}> help" )
    if sys.argv[1] == "dec" :
        decode()
    elif sys.argv[1] == "enc":
        encode()
    elif sys.argv[1]=="help":
        help()
    else:
        print("Invalid argurments. Please check the usage with help")
except Exception as e:
    print("")