import random
flag = b'WRECKIT50{hehehe_makasih_sudah_menebak_dan_menemani_belajar_fibonaci}'

ganjil = [1,3,5,7]
genap = [2,4,6,8]

x = random.randint(0,1606938044258990275541962092341162602522202993782792835301376)
y = random.randint(0,1606938044258990275541962092341162602522202993782792835301376)

print("Sekarang aku sedang bermain deret Fibonaci\r")
print("Dibutuhin basenya kan wkwkw, coba tebak\t")

while True:
    x_inp = int(input('S0? '))
    y_inp = int(input('S1? '))

    pad = ''
    if(x_inp==x and y_inp==y):
        print("Hehe benar itu")
        print(flag)
        break
    else:
        if(x_inp<x): pad = '\r'
        elif(x_inp==x): pad = ''
        else: pad = '\t'
        if(y_inp<y): pad = pad*random.choice(ganjil)
        elif(y_inp==y): pad = pad*0
        else: pad = pad*random.choice(genap)
        print("Masi salah bang >_<"+pad)