#Prime Number Checker
def primeNumber(number):
    is_prime=True
    for i in range(2,number):
        if number % 2==0:
            is_prime=False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

n=int(input("Enter the number to check prime or not"))
primeNumber(number=n)

#Paint Area Calulator
import math
def paint_area(height,width,cover):
    area = height*width
    TotalCans= math.ceil(area/cover)
    print(TotalCans)
paint_area(4,3,2)

#Caesar Cipher
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         newPosition=position+shift_amount
#         newLetter=alphabet[newPosition]
#         cipher_text+=newLetter
#     print(f"The encoded text is {cipher_text}")
#
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(plain_text=text,shift_amount=shift)
#Encryption and Decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position = position - shift_amount
        plain_text+=alphabet[new_position]
    print(f"The decode text is {plain_text}")
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text,shift_amount=shift)

