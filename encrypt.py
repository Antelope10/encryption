import helper as h
import random

def packet_encrypt(m, pub_key):
    m = h.convertToNumber(m) 
    n = int(pub_key.split('_')[0])
    e = int(pub_key.split('_')[1])
    md = pow(m,e,n)
    return md
def encrypt(m,pub_key):
    pointer = 0
    packets = []
    while pointer+12< len(m):
        packets.append(m[pointer:pointer+12])
        pointer += 12
    packets.append(m[pointer:len(m)])
    for packet in packets:
        packet = packet_encrypt(packet,pub_key)
    print(".".join(packets))
    return packets

def packet_decrypt(md, priv_key):
    md = int(md)
    n = int(priv_key.split('_')[0])
    d = int(priv_key.split('_')[1])
    m = pow(md,d,n)
    m = h.convertFromNumber(m)
def decrypt(md,priv_key):
    md = md.split(".")
    for packet in md:
        packet = packet_decrypt(packet,priv_key)
    m = "".join(md)
    print(m)
    return m

def generate_key_pair():
    p = int(random.randrange(1000000000000000,2000000000000000)) #generate p,q,n
    while not h.isPrime(p):
        p = p +1
    q = p+1
    while not h.isPrime(q):
        q += 1
    n = p*q
    
    totient_n = (q -1) * (p-1) #calculate totient(n)
    
    e = random.randrange(50,100) #generate e coprime to n
    while not h.coprime(totient_n,e):
        e += 1
        
    d = h.modinv(e,totient_n) #calculate modular inverse of e with respect to totient(n)
    
    public_key = str(n) + "_" + str(e)
    private_key = str(n)+ "_" + str(d)
    print("Public Key: " + public_key)
    print("Private Key: " + private_key)
    return public_key, private_key

def verifyKeys(pub_key, priv_key):
    testMessage = "hi12"
    out = encrypt(testMessage,pub_key)
    out = decrypt(out,priv_key)
    return out == testMessage

pub_key = 0
priv_key = 0

def main():
    while (1): #login/registration
        print("Type in the number of the action you want to take:")
        print("0 - Exit")
        print("1 - Login")
        print("2 - Register")
        action = input("Enter: ")
        if action == "0":
            return
        elif action == "1":
            pub_key = input("Public Key: ")
            priv_key = input("Private Key: ")
            if not verifyKeys(pub_key,priv_key):
                print("Invalid Login")
                pub_key = 0
                priv_key = 0
            else:
                exit = 1
        elif action == "2":
            pub_key, priv_key = generate_key_pair()
            exit = 1
        if exit:
            break  
    exit = 0
    
    while (1): #account actions   
        print("Type in the number of the action you want to take:")
        print("0 - Exit")
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Sign")
        action = int(input("Enter: "))
        if action == 0:
            return
        elif action == 1:
            encrypt(input("message: "),priv_key)
        elif action == 2:
            decrypt(input("cipher: "),pub_key)

if __name__ == "__main__":
    main()