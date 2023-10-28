import numpy as np

def encryption(plaintext, key_matrix):
    # 为numpy类型
    assert(type(key_matrix) is np.ndarray)
    # 为二维方阵
    assert(len(key_matrix.shape) == 2 and key_matrix.shape[0] == key_matrix.shape[1])
    # 为可逆矩阵
    assert(np.linalg.det(key_matrix) != 0)
    cipertext = ""
    pla_list = []
    pla_num = len(plaintext)
    # 转字母序数
    for char in plaintext:
        char_num = int(ord(char) - ord('a'))
        pla_list.append(char_num)
    # 补0做矩阵乘法
    while len(pla_list) % key_matrix.shape[0] != 0:
        pla_list.append(0)
    # 矩阵运算
    pla_matrix = np.array(pla_list).reshape(-1,len(key_matrix[0])).T
    cip_matrix = key_matrix @ pla_matrix
    cip_matrix = np.squeeze((cip_matrix.T).reshape(1,-1))
    # 字母序数还原
    for num in cip_matrix:
        char = chr(num % 26 + ord('A'))
        cipertext += char
    # 还原长度
    cipertext = cipertext[0:pla_num]
    return cipertext
    
