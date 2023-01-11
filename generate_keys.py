import random
import helper as h

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

def main():
    generate_key_pair()

if __name__ == "__main__":
    main()