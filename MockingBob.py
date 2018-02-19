user_input = ''
while True:
    message = ''
    case = 0
    user_input = input('Type in the message you want to put in MockingBob case (Type !exit to stop the program)\n>>')
    if user_input == '!exit':
        break
    for character in user_input:
        if character.isalpha():
            if case == 0:
                character = character.upper()
            else:
                character = character.lower()
            case = (case + 1) % 2
        message += character
    print(message)
