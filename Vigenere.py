import pdb

lower = 97
upper = 65


def encode(text=None, key=None):

    message = ''
    key_val = 0
    key_list = []

    for val in key:

        if val.isalpha():
            key_list += val

    for character in text:

        if character.isupper():
            key_val = key_val % len(key_list) + 1
            code = ord(character) + ord(key_list[key_val - 1].upper()) - upper

            if code >= upper + 26:
                code -= 26

            character = chr(code)

        elif character.islower():
            key_val = key_val % len(key_list) + 1
            code = ord(character) + ord(key_list[key_val - 1].lower()) - lower

            if code >= lower + 26:
                code -= 26

            character = chr(code)

        message += character

    print('Encoded message: ' + message)


def encode_no_space(text=None, key=None):

    message = ''
    key_val = 0
    key_list = []

    for val in key:

        if val.isalpha():
            key_list += val

    for character in text:

        if character.isalpha():
            key_val = key_val % len(key_list) + 1
            code = ord(character) + ord(key_list[key_val - 1].lower()) - lower

            if code >= lower + 26:
                code -= 26

            character = chr(code)
            message += character

        elif character.isdigit():
            message += character

    print('Encoded message: ' + message)


def decode(text=None, key=None):

    message = ''
    key_val = 0
    key_list = []

    for val in key:

        if val.isalpha():
            key_list += val

    for character in text:

        if character.isupper():
            key_val = key_val % len(key_list) + 1
            code = ord(character) - ord(key_list[key_val - 1].upper()) + upper

            if code < upper:
                code += 26

            character = chr(code)

        elif character.islower():
            key_val = key_val % len(key_list) + 1
            code = ord(character) - ord(key_list[key_val - 1].lower()) + lower

            if code < lower:
                code += 26

            character = chr(code)

        message += character

    print('Decoded message: ' + message)


def brute_force(text=None):

    decoded = False
    key = 'a'

    while decoded == False:

        if len(key) == 1:

            for i in range(26):

                key = chr(i + 97)
                message = ''
                key_val = 0

                for character in text:

                    if character.isupper():
                        key_val = key_val % len(key) + 1
                        code = ord(character) - ord(key[key_val - 1].upper()) + upper

                        if code < upper:
                            code += 26
                        character = chr(code)

                    elif character.islower():
                        key_val = key_val % len(key) + 1
                        code = ord(character) - ord(key[key_val - 1].lower()) + lower

                        if code < lower:
                            code += 26

                        character = chr(code)

                    message += character

                    if message == 'test':
                        print(f'Decoded message is: {message}')
                        print(f'Key used to encode was: {key[0]}')

        else:
            pass

        decoded = True


def dictionary_attack(text=None, loc=None):
    pass


while True:

    option = 0

    print('\nVigenere Encoder/Decoder\n[1] Encode\n[2] Decode\n[3] Encode (Alpha-numeric With No White Space)\n'
          '[4] Dictionary Attack (In Development) \n[5] Brute Force Attack (In Development)\n[8] Debug\n[9] Exit\n'
          '[0] More Information (Unwritten)')

    try:
        option = int(input(">>"))

    except ValueError:
        pass

    if option == 1:
        text = input('Input the text you want to encode\n>>')
        key = input('Create a secret key to encode the message with.\n>>').lower()
        encode(text, key)

    elif option == 2:
        text = input('Input the text you want to decode\n>>')
        key = input('Input the key you were given\n>>').lower()
        decode(text, key)

    elif option == 3:
        text = input('Input the text you want to encode\n>>').lower()
        key = input('Create a secret key to encode the message with.\n>>').lower()
        encode_no_space(text, key)

    elif option == 4:
        print("Sorry, this option doesn't exist yet.")
        """
        text = input('Input the text you want to run a dictionary attack on\n>>')
        loc = input('Please input the full path to the dictionary file location\n>>')
        dictionary_attack(text, loc)
        """

    elif option == 5:
        print("---------------------------------------------------")
        print("This option does not work yet, but is being tested.")
        print("---------------------------------------------------")
        print()
        text = input('Input the text you want to run a bruteforce attack on\n>>')
        brute_force(text)

    elif option == 8:
        pdb.run('debug')

    elif option == 9:
        exit()

    elif option == 0:
        print("Sorry, I don't have more info yet.")
