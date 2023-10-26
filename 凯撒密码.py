# 加密
def code(originaltext, key):
    ciphertext = ""
    for char in originaltext:
        if char == " ":
            ciphertext += " "
        else:
            ciphertext += chr((ord(char) - ord("a") + key) % 26 + ord("a"))
    return ciphertext

# 解密
def decode(ciphertext, key):
    originaltext = ""
    for char in ciphertext:
        if char == " ":
            originaltext += " "
        else:
            originaltext += chr((ord(char) - ord("A") - key) % 26 + ord("A"))
    return originaltext
    
print(decode("YMNX NX GTTP",5)) 