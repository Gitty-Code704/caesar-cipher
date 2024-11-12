# add your code here
text = "I'm a future Data Analyst!"
shift = 5

def caesar_cipher_right_shift_5(text): 
    result = ""
    shift = 5  # Shift of 5
    
    for char in text:
        # Uppercase Letters #ASCII Value "A"= 65
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Lowercase Letters #ACSII Value "a"= 97
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabet Characters
            result += char
    
    return result

cipher_text = caesar_cipher_right_shift_5(text) 
print("Original text:", text)
print("Ciphered text:", cipher_text)


