IP=[58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7]

IP_1=[40,8,48,16,56,24,64,32,
      39,7,47,15,55,23,63,31,
      38,6,46,14,54,22,62,30,
      37,5,45,13,53,21,61,29,
      36,4,44,12,52,20,60,28,
      35,3,43,11,51,19,59,27,
      34,2,42,10,50,18,58,26,
      33,1,41,9,49,17,57,25]

E=[32,1,2,3,4,5,             #扩展，将32bit数据扩展成48bit和子秘钥进行异或
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1]

S1=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
    0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
    4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
    15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]

S2=[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
    3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
    0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
    13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]

S3=[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
    13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
    13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
    1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

S4=[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
    13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
    10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
    3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]

S5=[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
    14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
    4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
    11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]

S6=[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
    10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
    9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
    4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

S7=[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
    13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
    1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
    6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]

S8=[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
    1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
    7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
    2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]

P=[16,7,20,21,
   29,12,28,17,
   1,15,23,26,
   5,18,31,10,
   2,8,24,14,
   32,27,3,9,
   19,13,30,6,
   22,11,4,25]

PC_1=[57,49,41,33,25,17,9,    #将64bit秘钥压缩成56bit
      1,58,50,42,34,26,18,
      10,2,59,51,43,35,27,
      19,11,3,60,52,44,36,
      63,55,47,39,31,23,15,
      7,62,54,46,38,30,22,
      14,6,61,53,45,37,29,
      21,13,5,28,20,12,4]

PC_2=[14,17,11,24,1,5,     #将56bit秘钥压缩成48bit
      3,28,15,6,21,10,
      23,19,12,4,26,8,
      16,7,27,20,13,2,
      41,52,31,37,47,55,
      30,40,51,45,33,48,
      44,49,39,56,34,53,
      46,42,50,36,29,32]

def str_bitarray(s):      #将字符串转换成二进制列表，从0开始
    b = ''.join([bin(ord(c)).replace('0b', '').zfill(8) for c in s])
    a = [int(m) for m in b]
    return a
def bitarray_str(s):    #将二进制列表转换成对应字母字符串
    for i in range(int(len(s) / 8) - 1):
        s.insert(8 * (i + 1) + i, ' ')
    s_then = [str(i) for i in s]
    mid = ''.join(s_then)
    return ''.join([chr(i) for i in [int(b, 2) for b in mid.split(' ')]])

def Left(A,a):   #将A列表中的内容循环左移a位
    for i in range(a):
        A.insert(len(A), A[0])
        A.remove(A[0])
    return A

def PC_2_Replace(subkey_mid):
    #print(len(subkey_mid))
    subkey_result=[subkey_mid[i-1] for i in PC_2]
    #print("PC_2置换后的长度"+str(len(subkey_result)))
    return subkey_result
def Subkey(Secret):      #求解子秘钥函数，并保存在列表中以备使用,Secret为二进制列表
    Secret_pc1=[Secret[i-1] for i in PC_1]      #对秘钥进行PC_1置换，将秘钥从64位压缩成56位
    #print("PC_1置换后的长度"+str(len(Secret_pc1)))
    Secret_left=Secret_pc1[:28]
    Secret_right=Secret_pc1[28:]
    #print(Secret_pc1,Secret_left,Secret_right)
    Subkey_result=[]
    for i in range(1,17):
        if(i==1 or i==2 or i==9 or i==16):
            Digit=1
        else:
            Digit=2
        #print(i,Digit)
        Secret_left=Left(Secret_left,Digit)
        Secret_right=Left(Secret_right,Digit)
        Secret_fin=PC_2_Replace(Secret_left+Secret_right)   #进行PC_2 转置
        #print(Secret_fin)
        Subkey_result.append(Secret_fin)
        #print("k"+str(i)+"形成")
    return Subkey_result

def E_extension(R):      #将32位的密匙扩展成48位，E扩展
    result=[R[i-1] for i in E]
    #print("E扩展为："+str(len(result)))
    return result
def S_box(a,S):    #S盒运算
    x=a[0]*2+a[5]*1
    y=a[1]*8+a[2]*4+a[3]*2+a[4]*1
    z=x*16+y
    # print("x:"+str(x)+"y:"+str(y))
    # print("------------")
    # print(z)
    # print(S[z])
    mid=bin(S[z])
    #print(mid)
    result=[]
    for i in mid[2:].rjust(4,'0'):
        result.append(int(i))
    #print(result)
    return result
def f(R,K):    #轮函数
    R=E_extension(R)
    #print(R)
    mid=[]
    for i in range(len(R)):   #将R和K逐位异或  存在mid列表中
        mid.append(R[i]^K[i])
    #print("R和K异或后mid位数："+str(len(mid)))
    a1=mid[:6]
    a2=mid[6:12]
    a3=mid[12:18]
    a4=mid[18:24]
    a5=mid[24:30]
    a6=mid[30:36]
    a7=mid[36:42]
    a8=mid[42:]
    #print(a1,a2,a3,a4,a5,a6,a7,a8)
    s1=S_box(a1,S1)
    s2=S_box(a2,S2)
    s3=S_box(a3,S3)
    s4=S_box(a4,S4)
    s5=S_box(a5,S5)
    s6=S_box(a6,S6)
    s7=S_box(a7,S7)
    s8=S_box(a8,S8)
    result_mid=s1+s2+s3+s4+s5+s6+s7+s8
    result=[result_mid[i-1] for i in P]
    #print(len(result))
    return result

def DES(Plaintext,key):   #DES加密
    #print("明文长度为:"+str(len(Plaintext)))
    Plaintext_first=[Plaintext[i-1] for i in IP]
    #print(len(Plaintext_first))
    L=Plaintext_first[:32]
    R=Plaintext_first[32:]
    sonkey=Subkey(str_bitarray(key))   #sonkey为子秘钥列表
    for i in range(0,15):   #DES十六轮循环
        mid=R
        f_result=f(R,sonkey[i])
        mid_mid=[]
        for i in range(len(f_result)):     #轮函数返回列表和L0逐位异或
            mid_mid.append(f_result[i]^L[i])
        R=mid_mid
        L=mid
    f_result=f(R,sonkey[15])
    mid_mid = []
    for i in range(len(f_result)):  # 轮函数返回列表和L0逐位异或
        mid_mid.append(f_result[i] ^ L[i])
    L=mid_mid
    result_mid=L+R
    result=[result_mid[m-1] for m in IP_1]
    return bitarray_str(result)

def DES_decrypt(Ciphertext,key):
    Plaintext_first = [Ciphertext[i - 1] for i in IP]
    #print(len(Plaintext_first))
    L = Plaintext_first[:32]
    R = Plaintext_first[32:]
    sonkey = Subkey(str_bitarray(key))  # sonkey为子秘钥列表
    for i in range(15, 0,-1):  # DES十六轮循环
        mid = R
        p_result = f(R, sonkey[i])
        mid_mid = []
        for i in range(len(p_result)):  # 轮函数返回列表和L0逐位异或
            mid_mid.append(p_result[i] ^ L[i])
        R = mid_mid
        L = mid
    p_result = f(R, sonkey[0])
    mid_mid = []
    for i in range(len(p_result)):  # 轮函数返回列表和L0逐位异或
        mid_mid.append(p_result[i] ^ L[i])
    L = mid_mid
    result_mid = L + R
    result = [result_mid[m - 1] for m in IP_1]
    return bitarray_str(result)

def do_encryption(inp):    #做加密
    print("请输入加密密匙（秘钥只能为8位）：")
    key=input()
    lens = len(inp) / 8
    if (lens - int(lens)) != 0:
        inp=inp.ljust((int(lens) + 1) * 8, ' ')
    result = ''
    for i in range(int(len(inp) / 8)):
        c = inp[0:8]
        inp = inp[8:]
        a = DES(str_bitarray(c),key)
        result = result + a
    return result

def do_decrypt(inp):    #做解密
    print("请输入解密密匙（秘钥只能为8位）：")
    key=input()
    lens = len(inp) / 8
    if (lens - int(lens)) != 0:
        inp = inp.ljust((int(lens) + 1) * 8, ' ')
    result = ''
    for i in range(int(len(inp) / 8)):
        c = inp[0:8]
        inp = inp[8:]
        a = DES_decrypt(str_bitarray(c),key)
        result = result + a
    return result

if __name__=="__main__":
    print("加密输入0    解密输入1：(加密解密内容不包含汉字)")
    flag=input()
    if(flag=='0'):
        print("请输入待加密的文件全名")
        jiami=input()
        #print(jiami)
        with open(jiami,"rb+") as fp:
            inp=fp.read().decode()
        #print(inp,type(inp))
        result=do_encryption(inp)
        print("加密结果为："+result)
        with open(jiami,"rb+") as fp:
            fp.seek(0)
            fp.truncate()   #清空文件
            fp.write(result.encode("utf-8"))
    if(flag=='1'):
        print("请输入待解密的文件全名")
        jiemi = input()
        #print(jiemi)
        with open(jiemi,"rb+") as fp:
            inp = fp.read().decode()
        result = do_decrypt(inp)
        print("解密结果为：" + result)
        with open(jiemi,"rb+") as fp:
            fp.seek(0)
            fp.truncate()   #清空文件
            fp.write(result.encode('utf-8'))

