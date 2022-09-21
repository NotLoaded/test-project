import os

os.remove("Encrypted_trojan.xmcl") 
os.chdir("./password-manager/")
os.remove("encryption.txt")
print('Removed!')

