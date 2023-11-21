
IP_table = [58,50,42,34,26,18,10,2,
            60,52,44,36,28,20,12,4,
            62,54,46,38,30,22,14,6,
            64,56,48,40,32,24,16,8,
            57,49,41,33,25,17,9,1,
            59,51,43,35,27,19,11,3,
            61,53,45,37,29,21,13,5,
            63,55,47,39,31,23,15,7]

# 初始置换
def InitialPermutation(plainbit):
    resbit = ""
    for index in IP_table:
        resbit += plainbit[index-1]
    L0 = resbit[0:32]
    R0 = resbit[32:64]
    return L0, R0

Shift_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

PermutationChoice1 = [57,49,41,33,25,17,9,1,
                      58,50,42,34,26,18,10,2,
                      59,51,43,35,27,19,11,3,
                      60,52,44,36,63,55,47,39,
                      31,23,15,7,62,54,46,38,
                      30,22,14,6,61,53,45,37,
                      29,21,13,5,28,20,12,4]

PermutationChoice2 = [14,17,11,24,1,5,
                      3,28,15,6,21,10,
                      23,19,12,4,26,8,
                      16,7,27,20,13,2,
                      41,52,31,37,47,55,
                      30,40,51,45,33,48,
                      44,49,39,56,34,53,
                      46,42,50,36,29,32]

def CircleMove(before, num, direction = "left"):
    assert(direction == "left" or direction == "right")
    if direction == "left":
        move_L = before[num:len(before)]
        move_R = before[0:num]
        return move_L + move_R
    else:
        move_R = before[0:len(before)-num]
        move_L = before[len(before)-num:len(before)]
        return move_L + move_R

# 生成子密钥
def gen_key(key):
    k0 = ""
    for index in PermutationChoice1:
        k0 += key[index-1]
    c0, d0 = k0[0:28], k0[28:56]
    CD_dict = {"C0":c0, "D0":d0}
    KEY_dict = {"K0":k0}
    for i in range(16):
        ci_val = CircleMove(CD_dict['C'+str(i)], Shift_table[i])
        di_val = CircleMove(CD_dict['D'+str(i)], Shift_table[i])
        ci, di = {'C'+str(i+1) : ci_val}, {'D'+str(i+1) : di_val}
        CD_dict.update(ci, di)
        ki_val = ""
        cd_val = ci_val + di_val
        for index in PermutationChoice2:
            ki_val += cd_val[index-1]
        ki = {'K'+str(i+1):ki_val}
        KEY_dict.update(ki)
    return KEY_dict

E_box = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]

S_boxes = {
    1: [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ],
    2: [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ],
    3: [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ],
    4: [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ],
    5: [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ],
    6: [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ],
    7: [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ],
    8: [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    ]
}

def Extend(Ri):
    R_E = []
    for index in E_box:
        R_E.append(Ri[index-1])
    return R_E

def Xor(Ri, Ki):
    R_X = ""
    for i in range(48):
        if Ri[i] == Ki[i]:
            R_X += '0'
        else:
            R_X += '1'
    return R_X

def Sreplace(Ri):
    index = 0
    R_res = ""
    while index < len(Ri):
        R_6bit = Ri[index, index+6]
        row = int(R_6bit[0]) * 2 + int(R_6bit[5])
        col = int(R_6bit[1:5], 2)
        R_res += bin(S_boxes[index/6+1][(row-1)*16+col-1])
    return R_res

p_box = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

def Place(Ri):
    R_P = ""
    for index in p_box:
        R_P+= Ri[index-1]
    return R_P

def Function(L0, R0, Keys, rounds = 16):
    LR_dict = {"L0":L0, "R0":R0}
    for i in range(rounds):
        Li = LR_dict['L'+str(i)]
        Ri = LR_dict['R'+str(i)]
        Lii = Ri
        Rii = Xor(Extend(Ri), Keys['K'+str(i+1)])
        Rii = Place(Sreplace(Rii))
        Rii = Xor(Rii, Li)
        LR_dict.update({'L'+str(i+1):Lii, 'R'+str(i+1):Rii})
    return LR_dict

LP_table = [  40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]

def LastPermutation(LR16):
    Res = ""
    for index in LP_table:
        Res += LR16[index-1]
    return Res

def encryption(plaintext, key):
    assert(len(key) == 64)
    L0, R0 = InitialPermutation(plaintext)
    Keys = gen_key(key)
    LR_dict = Function(L0, R0, Keys)
    LR_16 = LR_dict["L16"] + LR_dict["R16"]
    cipertext = LastPermutation(LR_16)
    return cipertext

print(encryption(""))