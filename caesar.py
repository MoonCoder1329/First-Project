
import math


caesarPass = True

while caesarPass:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  def caesar(start_text, shift_amount, cipher_direction):
    
    newPass = ""
    lastPass = ""
    for letter in start_text:
      newIndex = alphabet.index(letter) + shift_amount
      lastIndex = alphabet.index(letter) - shift_amount

      if lastIndex < (len(alphabet)*-1):
        while lastIndex <= len(alphabet)*-1:
          lastIndex +=len((alphabet))

      if newIndex > len(alphabet):
        while newIndex > len(alphabet):
          newIndex -= len(alphabet)

      newPass += alphabet[newIndex]
      lastPass += alphabet[lastIndex]
    if cipher_direction == "encode":
      print(f"The encoded text is {newPass}")
    elif cipher_direction == "decode":
      print(f"Decoded text : {lastPass}")
    else:
      print("Your cipher type is WRONG !! try again")
  caesar(start_text=text, shift_amount=shift, cipher_direction = direction)
  continueQuestion = input("do you want to continue Y / N ").lower()

  if continueQuestion == "n":
    print("Cipher program is closed. Goodbye ")
    caesarPass = False
    
  