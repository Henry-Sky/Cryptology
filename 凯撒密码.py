# 加密
def code(originaltext, key):
    key = (key % 26)
    ciphertext = ""
    for char in originaltext:
        org_ascii = (ord(char))
        if org_ascii >= 97 and org_ascii <= 122:
            cip_ascii = org_ascii - key
            if cip_ascii < 97:
                cip_ascii += 26
        elif org_ascii >= 65 and org_ascii <=90:
            cip_ascii = org_ascii - key
            if cip_ascii < 65:
                cip_ascii += 26
        else:
            cip_ascii = org_ascii
        ciphertext += chr(cip_ascii)
    return ciphertext

# 解密
def decode(ciphertext, key):
    key = (key % 26)
    originaltext = ""
    for char in ciphertext:
        cip_ascii = ord(char)
        if cip_ascii >= 97 and cip_ascii <= 122:
            org_ascii = cip_ascii + key
            if org_ascii >122:
                org_ascii -= 26
        elif cip_ascii >= 65 and cip_ascii <=90:
            org_ascii = cip_ascii + key
            if org_ascii > 90:
                org_ascii -= 26
        else:
            org_ascii = cip_ascii
        originaltext += chr(org_ascii)
    return originaltext
    
print(decode("YMNX NX GTTP",5)) 