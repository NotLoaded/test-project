import os
import zipfile
from datetime import datetime
import json
from colorama import Fore

print(Fore.RED + "Jay was here :) - 2022" + Fore.WHITE)

#DEFINE DIRECTORY VARIABLES

workspace = "./password-manager/"
filename = "encryption.txt"
filepath = os.path.join(workspace,filename)

encrypt = "null"

if not os.path.isdir(workspace):
    os.mkdir(workspace)


with open(filepath, "w") as file:
    file.write(encrypt)
    file.close()

my_zip = zipfile.ZipFile('encrypted.zip', 'w')
my_zip.write(workspace + "encryption.txt")
my_zip.close()

os.rename('encrypted.zip', "Encrypted_trojan.xmcl")