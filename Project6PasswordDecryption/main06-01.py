import itertools
passwd_string = "abcdefghijklmnopqrstuvwxyz0123456789"

for len in range(1, 4):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)