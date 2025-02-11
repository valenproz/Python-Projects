import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            passwd =''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode())
                print(f"The password is: {passwd}.")
                return 1
            except:
                pass

passwd_string = "abcdefghijklmnopqrstuvwxyz0123456789"

zFile = zipfile.ZipFile(r'Project6PasswordDecryption\passwd1234.zip')

min_len = 4
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result ==1:
    print("Password recovery was successful.")
else:
    print("Password recovery failed.")