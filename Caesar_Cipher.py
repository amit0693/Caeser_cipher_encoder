from ASCII_CEASER_CIPHER import  alphabet
from ASCII_CEASER_CIPHER import  logo
print(logo)
continue_further=True
def caesar (start_text, Shift_amount, cipher_direction):
    end_text=""
    if cipher_direction=='decode':
            Shift_amount *= -1  
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)  
            new_position=position+Shift_amount
            end_text+= alphabet[new_position]   
        else:
            end_text+= char
    print(f"The {cipher_direction} text is {end_text}")
while continue_further:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%25
    caesar(start_text=text, Shift_amount=shift, cipher_direction=direction)
    result=input("Type 'yes' if you want to go again. otherwise type no:")
    if result =='no':
        continue_further = False
        print("Goodbye")

