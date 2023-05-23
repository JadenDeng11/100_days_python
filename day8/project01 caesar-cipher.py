import logo
print(logo.logo)
print('Welcome to the CAESAR-CIPHER')

def encrypt(text01,shift01):
    new_text=""
    for letter in text01:
        if letter in logo.alphabet:
            position=logo.alphabet.index(letter)
            new_position=position+shift01
            new_letter=logo.alphabet[new_position]
            new_text+=new_letter
        else:
            new_text+=letter
    #         如果循环到的内容不在字母表里，不做任何处理直接+入new_text,接着继续for循环
    print(f"The encode text is:\n{new_text}")

def decrypt(text02,shift02):
    new_text=""
    for letter in text02:
        if letter in logo.alphabet:
            position=logo.alphabet.index(letter)
            new_position=position-shift02
            new_letter=logo.alphabet[new_position]
            new_text+=new_letter
        else:
            new_text+=letter
    print(f"The decode text is: \n{new_text}")

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    # 当shift超出26个字母

    if direction == 'encode':
        encrypt(text01=text,shift01=shift)
    elif direction == 'decode':
        decrypt(text02=text,shift02=shift)
    else:
        print('wrong input')

    restart=input('Do you want to restart? yes or no\n')
    if restart == 'yes':
        end=False
    elif restart == 'no':
        print('Goodbye!')
        end=True
    else:
        print('wrong input')
        end=True