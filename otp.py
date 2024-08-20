import random
def genotp():
    otp=''
    Caps=[chr(i) for i in range(ord('A'),ord('Z'))]
    sms=[chr(i) for i in range(ord('a'),ord('z'))]
    for i in range(0,2):   #loop will run 2 times.so it willl produce 6 letters otp
        otp=otp+random.choice(Caps)  #otp='K'
        otp=otp+str(random.randint(0,9)) #otp='K'+'3' #otp='K3'
        otp=otp+random.choice(sms)  #otp='K3'+'i'   #otp='K3i'
    print(otp)
    return otp
print(genotp())