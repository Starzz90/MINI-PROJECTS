def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

def main():
    while True:
        print('Hello This is the Caesar Decrypter!')
        print('Encrypt/Decrypt')

        try:
            option: str = input('Enter your option: ')
            if option == 'Encrypt':
                text = input('Enter your text: ')
                shift = int(input('Enter your shift: '))
                encrypted = encrypt(text, shift)
                print(f'Your encrypted text is {encrypted}')
            elif option == 'Decrypt':
                text = input('Enter your text: ')
                shift = int(input('Enter your shift: '))
                decrypted = decrypt(text, shift)
                print(f'Your decrypted text is {decrypted}')
            else:
                print('Invalid option.')
        except ValueError and TypeError:
            print('Please enter a proper option.')

if __name__ == '__main__':
    main()