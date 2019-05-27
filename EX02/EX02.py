def encode(message,shift):
    text = []
    if shift > 25 or shift < -25:
        shift = shift%26
    for i in message:
        letter = ord(i)+shift
        if ord(i) >= 65 and ord(i) <= 90:
            if letter > 90:
                letter = 64 + (letter - 90)
            elif letter < 65:
                letter = 89 - (65 - letter)
            text.append(chr(letter))
        elif ord(i) >= 97 and ord(i) <= 122:
            if letter > 122:
                letter = 96 + (letter - 122)
            elif letter < 97:
                letter = 121 - (97 - letter)
            text.append(chr(letter))
        else:
            text.append(i) 
    return "".join(text)
        
def crack(encoded_message,phrase):
    for i in range(0,25):
        decoded_message = encode(encoded_message, -i)
        print(decoded_message)
        if phrase in decoded_message:
            return decoded_message

print(encode("TeRe!!", 25))
