import random, time

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
lenght = int(input("Введите длину случайного пароля:"))
print(" ")
print("Случайно созданный пароль:")
time.sleep(1.5)

for i in range(lenght):
    password += random.choice(characters)

print(password)
