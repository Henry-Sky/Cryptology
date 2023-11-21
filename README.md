# 密码学:Cryptology

### 信息安全:
信息安全是一种维护信息的机密性，完整性和可用性的过程，旨在保护信息免受未经授权的访问、使用、披露、修改、破坏或者中断

[名词解释](https://github.com/Henry-Sky/Cryptology/blob/master/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8/%E5%90%8D%E8%AF%8D%E8%A7%A3%E9%87%8A.md)
[协议](https://github.com/Henry-Sky/Cryptology/blob/master/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8/%E5%8D%8F%E8%AE%AE.md)
[算法](https://github.com/Henry-Sky/Cryptology/blob/master/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8/%E7%AE%97%E6%B3%95.md)
[应用](https://github.com/Henry-Sky/Cryptology/blob/master/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8/%E5%BA%94%E7%94%A8.md)
[技术](https://github.com/Henry-Sky/Cryptology/blob/master/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8/%E6%8A%80%E6%9C%AF.md)

### 密码学发展简史:
- 古典密码学阶段：

    1. 凯撒密码  
    2. 维吉尼亚密码

- 近代密码时期：
 
    1. Vernam密码  
    2. 轮转密码

- 现代密码学阶段：

    1. DES
    2. AES
    3. RC4
    4. RSA

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
