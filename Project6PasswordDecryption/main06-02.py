import itertools
import zipfile

passwd_string = "abcdefghijklmnopqrstuvwxyz0123456789"
#Compressed file path
zFile = zipfile.ZipFile(r'Project6PasswordDecryption\passwd1234.zip')

for len in range(1,6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd=passwd.encode())
            print (f"The password is {passwd}.")
            break
        except:
            pass