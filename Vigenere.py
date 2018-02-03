import pdb

lower = 97
upper = 65


def encode(text=None, key=None):
    message = ''
    key_val = 0
    key_list = []

    for val in key:
        if val != ' ':
            key_list += val

    for letter in text:
        key_val = key_val % len(key) + 1
        if letter.isupper():
            code = ord(letter) + ord(key_list[key_val - 1].upper()) - upper
            if code >= upper + 26:
                code -= 26
            letter = chr(code)
        elif letter.islower():
            code = ord(letter) + ord(key_list[key_val - 1].lower()) - lower
            if code >= lower + 26:
                code -= 26
            letter = chr(code)
        message += letter
    print('Encoded message: ' + message)


def encode_no_space(text=None, key=None):
    message = ''
    key_val = 0
    key_list = []

    for val in key:
        if val != ' ':
            key_list += val

    for letter in text:
        if letter.isalpha():
            key_val = key_val % len(key) + 1
            code = ord(letter) + ord(key_list[key_val - 1].lower()) - lower
            if code >= lower + 26:
                code -= 26
            letter = chr(code)
            message += letter
        elif letter.isdigit():
            message += letter
    print('Encoded message: ' + message)


def decode(text=None, key=None):
    message = ''
    key_val = 0
    key_list = []

    for val in key:
        if val != ' ':
            key_list += val

    for letter in text:
        key_val = key_val % len(key) + 1
        if letter.isupper():
            code = ord(letter) - ord(key_list[key_val - 1].upper()) + upper
            if code < upper:
                code += 26
            letter = chr(code)
        elif letter.islower():
            code = ord(letter) - ord(key_list[key_val - 1].lower()) + lower
            if code < lower:
                code += 26
            letter = chr(code)
        message += letter
    print('Decoded message: ' + message)

while True:
    option = 0

    print("\nVigenere Encoder/Decoder\n[1] Decode\n[2] Encode (Default)\n[3] Encode (Alnum with no white space)\n[8] Debug\n[9] Exit")
    try:
        option = int(input(">>"))
    except ValueError:
        pass

    if option == 1:
        text = input("Input the text you want to decode\n>>")
        key = input("Input the key you were given\n>>")
        decode(text, key)
    elif option == 2:
        text = input('Input the text you want to encode\n>>')
        key = input('Input your secret key\n>>')
        encode(text, key)
    elif option == 3:
        text = input('Input the text you want to encode\n>>').lower()
        key = input('Input your secret key\n>>').lower()
        encode_no_space(text, key)
    elif option == 8:
        pdb.run("debug")
    elif option == 9:
        exit()