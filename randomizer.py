import random
import string

if __name__ == '__main__':
    charset = string.letters + string.digits + '!@#$%^*'
    password_length = random.randint(12,16)
    password = ''

    for i in range(0, password_length):
        password += charset[random.randint(0,len(charset)-1)]

    print password