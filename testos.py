import time
import os, platform

jls_extract_var = """
████████████████████████████████████
█─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█─▄▄─█─▄▄▄▄█
███─████─▄█▀█▄▄▄▄─███─███─██─█▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀
"""
print(jls_extract_var)


jls_extract_var = """
[1] Contunie with TestOS setup
[2] I Have Already Done TestOS Setup
"""
print(jls_extract_var)
setup = input(":")
if setup == '1':
    name = input(str("Enter your name to display: "))
    pas = input(str("Enter your password to login: "))

    lines = [name]

    if not os.path.exists("user"): # Checks if folder doesn't exist
        os.mkdir("user") # Create folder if doesn't exist

    with open("user/username.txt", "w") as f:
        f.writelines(name)

    lines4 = [pas]
    with open('user/password.txt', 'w') as f:
        f.writelines(pas)
    print("TESTOS Setup has been Completed!!!")
    time.sleep(1)
    if platform.system() == "Darwin":
      os.system("open home.py")
    elif platform.system() == "Windows":
        os.startfile('home.py')
    elif platform.system() == "Linux":
        os.system("xdg-open home.py")
    else:
         print("Host OS unsupported.")
    exit()

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

else: # If no input then exit the program
    exit()

while True:
    login = input(str("Enter your password To " + l_n + ": "))
    if login == l_p:
        if platform.system() == "Darwin":
          os.system("open home.py")
        elif platform.system() == "Windows":
            os.startfile("home.py")
        elif platform.system() == "Linux":
            os.system("xdg-open home.py")
        else:
             print("Host OS unsupported.")
        break
    else:
        print("Wrong password!")
