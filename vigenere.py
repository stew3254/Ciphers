import pdb

lower = 97
upper = 65
common_words = ['that', 'with', 'they', 'have', 'this', 'from', 'some', 'what', 'there', 'other', 'were', 'your',
                'when', 'word', 'said', 'each', 'which', 'their', 'time', 'will', 'about', 'many', 'then', 'them',
                'would', 'write', 'like', 'these', 'long', 'make', 'thing', 'look', 'more', 'could', 'come', 'sound',
                'most', 'number', 'over', 'know', 'water', 'than', 'call', 'first', 'people', 'down', 'side', 'been',
                'find', 'work', 'part', 'take', 'place', 'made', 'live', 'where', 'after', 'back', 'little', 'only',
                'round', 'year', 'came', 'show', 'every', 'good', 'give', 'under', 'name', 'very', 'through', 'just',
                'form', 'much', 'great', 'think', 'help', 'line', 'before', 'turn', 'cause', 'same', 'mean', 'differ',
                'move', 'right', 'does', 'tell', 'sentence', 'three', 'want', 'well', 'also', 'play', 'small', 'home',
                'read', 'hand', 'port', 'large', 'spell', 'even', 'land', 'here', 'must', 'high', 'such', 'follow',
                'change', 'went', 'light', 'kind', 'need', 'house', 'picture', 'again', 'animal', 'point', 'mother',
                'world', 'near', 'build', 'self', 'earth', 'father', 'head', 'stand', 'page', 'should', 'country',
                'found', 'answer', 'school', 'grow', 'study', 'still', 'learn', 'plant', 'cover', 'food', 'four',
                'thought', 'keep', 'never', 'last', 'door', 'between', 'city', 'tree', 'cross', 'since', 'hard',
                'start', 'might', 'story', 'draw', 'left', 'late', "don't", 'while', 'press', 'close', 'night', 'real',
                'life', 'stop']


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
    key_list = ['a']
    pos = len(key_list) - 1
    tries = 0
    common = 0

    while decoded == False:

        message = ''
        key_val = 0

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

        tries += 1

        for word in common_words:

            if word in message.lower():
                common += 1

            if common > 1:
                key = ''
                for letter in key_list:
                    key += letter
                answer = input(f'Does this look like the decoded message? (y/n)\n{message}\n>>')
                if answer.lower() == 'y':
                    print(f'\nThe message is: {message}')
                    print(f'The key used to encode was: {key}')
                    print(f'Keys attempted: {tries}')
                    decoded = True
                elif answer.lower() == 'n':
                    print('Okay, I will continue decoding!')
                    common = 0
                else:
                    print('Please enter either y or n')

        if common > 0:
            key = ''
            for letter in key_list:
                key += letter
            answer = input(f'Does this look like the decoded message? (y/n)\n{message}\n>>')
            if answer.lower() == 'y':
                print(f'\nThe message is: {message}')
                print(f'The key used to encode was: {key}')
                print(f'Keys attempted: {tries}')
                decoded = True
            elif answer.lower() == 'n':
                print('Okay, I will continue decoding!')
            else:
                print('Please enter either y or n')


        else:
            key_list[pos] = chr(ord(key_list[pos]) + 1)
            while ord(key_list[pos]) > ord('z'):
                pos -= 1

                if pos < 0:
                    key_list += 'a'

                    for x in range(len(key_list)):
                        key_list[x] = 'a'

                    pos = len(key_list) - 1

                else:

                    for x in range(len(key_list)):

                        if x > pos:
                            key_list[x] = 'a'

                    key_list[pos] = chr(ord(key_list[pos]) + 1)

                    if ord(key_list[pos]) <= ord('z'):
                        pos = len(key_list) - 1

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
        print("------------------------------------------------")
        print("This option somewhat works, and is being tested.")
        print("------------------------------------------------")
        print()
        text = input('Input the text you want to run a bruteforce attack on\n>>')
        brute_force(text)

    elif option == 8:
        pdb.run('debug')

    elif option == 9:
        exit()

    elif option == 0:
        print("Sorry, I don't have more info yet.")
