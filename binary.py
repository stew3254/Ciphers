import pdb


def encode(message=None, space=False):
    binary_message = ''
    if message is None:
        message = input('Input the message you want to convert to binary: ')
    for character in message:
        binary = bin(ord(character))[2:]
        if space is True:
            binary_message += ' %08d' % int(binary)
        else:
            binary_message += '%08d' % int(binary)
    print('>>' + binary_message.strip())


def encode_with_formatting(message=None, space=False):
    binary_message = ''
    if message is None:
        message = input('Input the message you want to convert to binary: ')
    for character in message:
        binary = bin(ord(character))[2:]
        if space is True:
            binary_message += ' 0b%08d' % int(binary)
        else:
            binary_message += '0b%08d' % int(binary)
    print('>>' + binary_message.strip())


def decode(binary_message=None):
    message = ''
    characters = []
    if binary_message is None:
        binary_message = input('Input the binary you want to convert into a message: ').strip()
    if '0b' in binary_message and ' ' in binary_message:
        characters = binary_message.split()
        for i in range(len(characters)):
            characters[i] = characters[i][2:]
        for i in range(len(characters)):
            character = chr(int(characters[i], 2))
            message += character
    elif '0b' in binary_message:
        characters = binary_message.split('0b')
        characters.pop(0)
        for i in range(len(characters)):
            character = chr(int(characters[i], 2))
            message += character
    elif ' ' in binary_message:
        characters = binary_message.split()
        for i in range(len(characters)):
            character = chr(int(characters[i], 2))
            message += character
    else:
        for character in binary_message:
            characters += character
        for i in range(int(len(binary_message)/8)):
            character = ''
            num = i*8
            for x in range(8):
                character += characters[num]
                num +=1
            character = chr(int(character, 2))
            message += character
    print('>>' + message.strip())

option = 0

while option != 4:
    try:
        option = int(input('Binary Encoder / Decoder\n[1] Encode\n[2] Decode\n[3] Debug\n[4] Exit\n>>'))
    except:
        print('You must choose one of the numbers in the list')
    if option == 1:
        print()
        encode()
        print()
    elif option == 2:
        print()
        decode()
        print()
    elif option == 3:
        print()
        pdb.run('Debug')
        print()
