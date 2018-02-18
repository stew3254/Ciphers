import pdb


def encode_no_space(message=None):
    hexadecimal_message = ''
    if message is None:
        message = input('Input the message you want to convert to hexadecimal: ')
        print(message)
    for character in message:
        hexadecimal = str(hex(ord(character))[2:])
        try:
            hexadecimal_message += '%02d' % int(hexadecimal)
        except:
            hexadecimal_message += hexadecimal
    print('>>' + hexadecimal_message.strip())


def encode_with_space(message=None):
    hexadecimal_message = ''
    if message is None:
        message = input('Input the message you want to convert to hexadecimal: ')
        print(message)
    for character in message:
        hexadecimal = str(hex(ord(character))[2:])
        try:
            hexadecimal_message += ' %02d' % int(hexadecimal)
        except:
            hexadecimal_message += ' ' + hexadecimal
    print('>>' + hexadecimal_message.strip())


def encode_with_formatting_no_space(message=None):
    hexadecimal_message = ''
    if message is None:
        message = input('Input the message you want to convert to hexadecimal: ')
        print(message)
    for character in message:
        hexadecimal = hex(ord(character))
        hexadecimal_message += hexadecimal
    print('>>' + hexadecimal_message.strip())


def encode_with_formatting_with_space(message=None):
    hexadecimal_message = ''
    if message is None:
        message = input('Input the message you want to convert to hexadecimal: ')
        print(message)
    for character in message:
        hexadecimal = hex(ord(character))
        hexadecimal_message += ' ' + hexadecimal
    print('>>' + hexadecimal_message.strip())


def decode(hexadecimal_message=None):
    message = ''
    characters = []
    if hexadecimal_message is None:
        hexadecimal_message = input('Input the hexadecimal you want to convert into a message: ').strip()
    if '0x' in hexadecimal_message and ' ' in hexadecimal_message:
        characters = hexadecimal_message.strip().split()
        for i in range(len(characters)):
            characters[i] = characters[i][2:]
        for i in range(len(characters)):
            character = chr(int(characters[i], 16))
            message += character
    elif '0x' in hexadecimal_message:
        characters = hexadecimal_message.split('0x')
        characters.pop(0)
        for i in range(len(characters)):
            character = chr(int(characters[i], 16))
            message += character
    elif ' ' in hexadecimal_message:
        characters = hexadecimal_message.split()
        for i in range(len(characters)):
            character = chr(int(characters[i], 16))
            message += character
    else:
        for character in hexadecimal_message:
            characters += character
        for i in range(int(len(hexadecimal_message)/2)):
            character = ''
            num = i*2
            for x in range(2):
                character += characters[num]
                num +=1
            character = chr(int(character, 16))
            message += character
    print('>>' + message.strip())

option = 0

while option != 4:
    try:
        option = int(input('Hexadecimal Encoder / Decoder\n[1] Encode\n[2] Decode\n[3] Debug\n[4] Exit\n>>'))
    except:
        print('You must choose one of the numbers in the list')
    if option == 1:
        print()
        encode_no_space()
        print()
    elif option == 2:
        print()
        decode()
        print()
    elif option == 3:
        print()
        pdb.run('Debug')
        print()
