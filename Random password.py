import random
Password = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_€£¥₩!@#$%^&*)(?:-!')

length = int(input('Enter the lenght of the password: '))

com = "".join(random.sample(Password, length))

print(com)
