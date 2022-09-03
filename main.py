alphabet = ("abcdefghijklmnopqrstuvwxyz")

user = str(input("Do you want to encrypt (1) or decrypt (2)? "))
key = int(input("Enter the key the code is going to be using: "))

def caesar_encrypt(str, key):
    str = str.lower()
    str_list = list(str)
    for i in range (len(str_list)):       
        index = alphabet.find(str_list[i])
        if str_list[i] == " ":
            str_list[i] =  " "
        elif (index+key) <= 26:
            str_list[i] = alphabet[index+key]
        else:
            str_list[i] = alphabet[(index + key) % 26]
            print("b")

    print(''.join(str_list))


def caesar_decrypt(str, key):
    str = str.lower()
    str_list = list(str)
    for i in range(len(str_list)):
        index = alphabet.find(str_list[i])
        if str[i] == " ":
            str_list = " "
        else: 
            str_list[i] = alphabet[(index - key) % 26]
    print(''.join(str_list))

if user == "1":
    mssg_to_encrypt = input("Enter the message you want to encrypt: ")
    caesar_encrypt(mssg_to_encrypt, key)

elif user == "2":
    mssg_to_decrypt = input("Enter the message you want to decrypt: ")
    caesar_decrypt(mssg_to_decrypt, key)
