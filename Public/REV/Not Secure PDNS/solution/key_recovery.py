from pwn import *
from Crypto.Util.number import *
from sage.rings.factorint import factor_trial_division
from sympy.ntheory.modular import crt 
import time
from math import gcd
import requests

url = 'http://137.184.250.54:5555/encrypt'

hasil = []
for coun in range(100):
    try:
        def sendMessage(arr_x):
            sendata = b''
            for i in arr_x:
                sendata+=i.encode()+b'\n'
            sendata = sendata[:-1]
            filedata = {'file': sendata}
            resp = requests.post(url, files=filedata)
            result = []
            p = int(resp.content.split(b'--PUBS--')[1].split(b'--END--')[0].decode(),16)
            # print(resp.content)
            # exit(1)
            for i in resp.content.split(b'--START--')[1:]:
                respdata = i.split(b'--END--\n')[0]
                result.append(int(respdata.decode(),16))
            return p, result

        init_message = "plays"

        arrInp = [init_message]

        p, out_ret= sendMessage(arrInp)
        
        print("Getting out_ret")
        initiation = out_ret[0]

        assert isPrime(p)
        limitNum = 100000
        fact = factor_trial_division(p-1, limitNum)

        def solvePoligh(arr, pr):
            res = []
            for i in arr:
                justOne = False
                appends = None
                for j in range(1, i[2]):
                    if(pow(i[1], j, pr)==pow(i[0], 1, pr)):
                        if(justOne):
                            justOne = False
                            break
                        else:
                            appends = [j, i[2]]
                            justOne = True
                if(justOne): res.append(appends)
            return res
        
        # format list for poligh solve
        # [(g, h, pe)]
        lp = []
        count = [bytes_to_long(init_message.encode()), initiation]
        for i,j in fact:
            if pow(i,j)<limitNum:
                pe = pow(i, j)
                g = pow(count[1],((p-1)//pe), p)
                h = pow(count[0],((p-1)//pe), p)
                # handling no gcd with phi
                if(g==h or g==1 or h==1 or gcd(h,p-1)!=1 or gcd(g,p-1)!=1): 
                    pass
                else:
                    lp.append([g,h,pe])

        result = solvePoligh(lp, p)
        hasil += result
        # print(count,":",result)
        # io.close()
    except Exception as error:
        print("An error occurred:", error)

m = []
v = []
for i,j in hasil: 
    m.append(i)
    v.append(j)

crt_m = crt(v,m)
keys = int(crt_m[0])
print(keys)
p, out_ret= sendMessage(["ini coba plain"])
dec_key = pow(keys, -1, p-1)

from Crypto.Util.number import long_to_bytes
plain = int(pow(int(out_ret[0]), dec_key, p))
print(plain)
print(long_to_bytes(plain))

# target = 149288500468776648188046808125977264807
# for i in range(len(m)):
#     if(target%v[i]!=m[i]): 
#         print("nah lo", m[i], v[i])