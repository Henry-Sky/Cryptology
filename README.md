# 密码学:Cryptology


### (1) 凯斯密码:Caesar.py
key 为数字, 表示字母表移位
- 加密: ci = (pi - ki) mod 26
- 解密: pi = (ci + ki) mod 26

### (2) 单词表密码:WordTable.py
key 为单词,重排列26个字母表,决定加解密对应关系

### (3) 维吉尼亚密码:Vigenere.py
key 为单词, 循环使用该单词
- 加密: ci = (pi + ki) mod 26
- 解密: pi = (ci - ki) mod 26

### (4) 普莱费尔密码:Playfair.py
由 key 决定一个5x5的密码矩阵，一般 j 由 i 代替

### (5) 希尔密码:Hill.py
原文奇数位末尾补约定字符,或原文中连续重复字母中间插入约定字符
- 加密: mat_k * mat_p
- 解密: 待做(Todo)

### (6) DES加密:DES.py
分组加密算法, 16轮扩展,混淆,压缩
- 加密: 待测试
- 解密: 待做(Todo)
