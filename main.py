encode_loop = True

def decode(decode_str):                             # decodes password
    password_str = ''
    for i in decode_str:
        if i == '0':
            str(password_str)
            password_str += '7'
        elif i == '1':
            str(password_str)
            password_str += '8'
        elif i == '2':
            str(password_str)
            password_str += '9'
        else:
            password_str += str(int(i) - 3)
    return password_str


def encode():                                       # encodes function
    pass


def main():
    while encode_loop:                              # ensures menu keeps repeating
        print('Menu\n' +
              '-------------\n' +
              '1. Encode\n' +
              '2. Decode\n' +
              '3. Quit')

        menu_option = int(input('Please enter an option: '))
        password_str = input('Please enter your password to encode: ')

        if menu_option == 1:
            encoded_password = encode(password_str)
            print('Your password has been encoded and stored!')
        elif menu_option == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {password_str}.')
        elif menu_option == 3:
            break



if __name__ == '__main__':
    main()

