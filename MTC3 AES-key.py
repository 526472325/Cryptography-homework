import hashlib
import binascii
import base64
from Crypto.Cipher import AES
data = "12345678<8<<<1110182<1111167<<<<<<<<<<<<<<<4"
data = data[:10]+data[13:20]+data[21:28]
print(data,"data")

H_information = hashlib.sha1(data.encode()).hexdigest()
print(H_information,"H_information")
K_seed = H_information[:32]# 取前16字节
print(K_seed,"K_seed")

c ="00000001"
d = K_seed + c

H_d = hashlib.sha1(bytes.fromhex(d)).hexdigest()
ka = H_d[:16]
kb = H_d[16:32]

#奇偶校验位的判断
def jiaoyan(x):
    k = []
    a = bin(int(x,16))[2:]
    for i in range(0,len(a),8):
        if (a[i:i+7].count("1"))%2 == 0:
            k.append(a[i:i+7])
            k.append('1')
        else :
            k.append(a[i:i+7])
            k.append('0')
    a1 = hex(int(''.join(k),2))
    return a1[2:]

k_1 = jiaoyan(ka)
k_2 = jiaoyan(kb)
key = k_1 + k_2
print(key,"key")

s = """9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jx
aa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2N
fNnWFBTXyf7SDI"""
cipher = base64.b64decode(s)
IV = b"\x00"*AES.block_size
m=AES.new(binascii.unhexlify(key),AES.MODE_CBC,IV)
print(m.decrypt(cipher).decode())