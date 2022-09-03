alphabet = ("abcdefghijklmnopqrstuvwxyz")

user = str(input("Do you want to encrypt (1) or decrypt (2)? "))
shift = int(input("Enter the shift: "))

def caesar_encrypt(str, key):
    str = str.lower()
    str_list = list(str)
    for i in range (len(str_list)):       
        index = alphabet.find(str_list[i])
        if str_list[i] == " ":
            str_list[i] =  " "
        elif (index+shift) <= 25:
            str_list[i] = alphabet[index+shift]
        elif (index+shift) > 25:
            str_list[i] = alphabet[(index + shift) % 25]

    print(''.join(str_list))


def caesar_decrypt(str, key):
    str = str.lower()
    str_list = list(str)
    for i in range(len(str_list)):
        index = alphabet.find(str_list[i])
        if str[i] == " ":
            str_list[i] = " "
        elif (index-shift) >= 0:
            str_list[i] = alphabet[(index - shift)]
        elif (index-shift) < 0: 
            str_list[i] = alphabet[(index - shift) % 26]
    
    print(''.join(str_list))

if user == "1":
    mssg_to_encrypt = input("Enter the message you want to encrypt: ")
    caesar_encrypt(mssg_to_encrypt, shift)

elif user == "2":
    mssg_to_decrypt = input("Enter the message you want to decrypt: ")
    caesar_decrypt(mssg_to_decrypt, shift)
