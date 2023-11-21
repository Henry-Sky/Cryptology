def gen_table(key_word, reverse = False):
    uni_word = []
    for i in key_word:
        if i.upper() not in uni_word:
            uni_word.append(i.upper())
    en_table = {}
    de_table = {}
    for i in range(65, 91):
        if chr(i) not in uni_word:
            uni_word.append(chr(i))
        en_table.update({chr(i+32) : uni_word[i - 65]})
        de_table.update({uni_word[i - 65] : chr(i+32)})
    if reverse:
        return de_table
    else:
        return en_table

def encryption(plaintext, key_word):
    cipertext = ""
    table = gen_table(key_word)
    for a in plaintext:
        cipertext += table[a]
    return cipertext

def decryption(cipertext, key_word):
    plaintext = ""
    table = gen_table(key_word, reverse=True)
    for a in cipertext:
        plaintext += table[a]
    return plaintext