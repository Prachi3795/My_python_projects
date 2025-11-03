#Code for password management, which saves and user account and its associated password.

from cryptography.fernet import Fernet
import base64, hashlib

def write_key():
 key= Fernet.generate_key()
 with open("key.key", "wb") as key_file:
  key_file.write(key)


def load_key():
 
 file =open("key.key","rb")

 key=file.read()
 file.close()
 return key


master_pwd =input("What is the master password?\n")
raw_key = load_key()
derived = hashlib.sha256(raw_key + master_pwd.encode()).digest()
key = base64.urlsafe_b64encode(derived)
fer = Fernet(key)
'''key=load_key() + master_pwd.encode()
fer=Fernet(key)'''

def view():
 with open("password.txt",'r') as f:
  for line in f.readlines():
   data=line.rstrip()
   user, passw=data.split("|")
   print("User:", user, "Password:", fer.decrypt(passw.encode()).decode())
 
def add():
 name=input("Account Name: \n")
 pwd=input("Password: \n")

 with open("password.txt",'a') as f:
  f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
 
while True:
   mode=input("Would you like to add new password or view existing ones? a.add  b.view c.quit \n").lower()
   if mode=="quit":
    break
   if mode=="view":
    view()
   elif mode=="add":
    add()
   else:

    print("Invalid mode.\n")
    continue