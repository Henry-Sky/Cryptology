def encryption(plaintext, key_word):
    index = 0
    cipertext = ""
    while index < len(plaintext):
        pla_char = plaintext[index]
        key_char = key_word[index%len(key_word)]
        cip_char = chr((ord(pla_char) - ord('a') + ord(key_char) - ord('a')) % 26 + ord('a'))
        cipertext += cip_char.upper()
        index += 1
    return cipertext

def decryption(cipertext, key_word):
    index = 0
    plaintext = ""
    while index < len(cipertext):
        cip_char = cipertext[index]
        key_char = key_word[index%len(key_word)].upper()
        pla_char = chr((ord(cip_char) - ord(key_char)) % 26 + ord('A'))
        plaintext += pla_char.lower()
        index += 1
    return plaintext