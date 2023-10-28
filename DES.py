
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

k = ""
print(len(k))
keys = gen_key(k)



