import random
import string

chars = " "+ string.whitespace + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)


# print(f"chars: {chars}")
# print(f"key: {key}")

#Encryption 

user_text = input("Enter a message to encrypt : ")
encrypt_text = ""

for text in user_text:
    index = chars.index(text)
    encrypt_text += key[index]

print(f"Your message is :{user_text}")
print(f"The encrypted message is : {encrypt_text}")


