# 根据密钥建立密码表(I表示I/J)
def gen_matrix(key_word):
    word_list = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    uni_key = []
    # 密钥去重，去空格
    for char in key_word:
        if char == 'j':
            char = 'i'
        if (char.upper() not in uni_key
            and char != ' '):
            uni_key.append(char.upper())
    # 新字母表创建
    for char in word_list:
        if char.upper() not in uni_key:
            uni_key.append(char.upper())
    key_mat = []
    for row in range(5):
        row_list = []
        for col in range(5):
            row_list.append(uni_key[row*5+col])
        key_mat.append(row_list)
    return key_mat
 
# 获取字符在密码表中的位置
def get_index(char, key_mat):
    for row in range(5):
        for col in range(5):
            if char.upper() == key_mat[row][col]:
                return row, col

def encryption(plaintext, key_word):
    plaintext = plaintext.replace(' ','')
    key_mat = gen_matrix(key_word)
    cipertext = ""
    index = 0
    while index < len(plaintext):
        if index + 1 <len(plaintext):
            p1, p2 = plaintext[index], plaintext[index + 1]
            if p1 == p2:
                # p1, p2重复,中间插入p1后面一个字母
                # extra_p = chr((ord(p1) - ord("a") + 1) % 26 + ord("a"))
                extra_p = 'x'
                plaintext = plaintext[0:index+1] + extra_p + plaintext[index+1:len(plaintext)+1]
                # index不移动,重新进入判断
                continue
            row1, col1 = get_index(p1, key_mat)
            row2, col2 = get_index(p2, key_mat)
            if row1 == row2:
                # 同一行,右移
                c1 = key_mat[row1][(col1 + 1) % 5]
                c2 = key_mat[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # 同一列,下移
                c1 = key_mat[(row1 + 1) % 5][col1]
                c2 = key_mat[(row2 + 1) % 5][col2]
            else:
                # 矩形对角
                c1 = key_mat[row1][col2]
                c2 = key_mat[row2][col1]
            cipertext += (c1 + c2 + ' ')
        else:
            # 原文字符为奇数个，补一个末尾字符的后一位
            end_chr = plaintext[index]
            plaintext += 'z'
            # plaintext += chr((ord(end_chr) - ord("a") + 1) % 26 + ord("a"))
            continue
        index += 2
    return cipertext

print(encryption('happymonday','weekday'))