alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Caesar function
def caesar(text_c, shift_c, direction_c):
  final_text = ""
  if direction == "decode":
    shift_c *= -1 
  elif direction == "encode":
    shift_c 
  for letter in text_c: 
    if letter in alphabet:
      alpha_index = alphabet.index(letter)
      shift_index = alpha_index + shift_c
      if shift_index > (len(alphabet)-1):  #index out of range bug
        shift_index -= (len(alphabet))
      elif shift_index < 0:
        shift_index += (len(alphabet))
      final_text += alphabet[shift_index] 
    else:
      final_text += letter  
  print(f"The {direction}d text is {final_text}")

from art import logo
print(logo)

#loop to restart or end program
while True:
  restart = input("Do you want to restart the cipher program? Type 'yes' or 'no'.\n").lower()
  if (restart == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
  else:
     break 
