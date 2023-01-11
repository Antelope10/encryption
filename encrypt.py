import random
import helper as h
import sys

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
    for i in range(len(packets)):
        packets[i] = str(packet_encrypt(packets[i],pub_key))
    print(".".join(packets))
    return ".".join(packets)

def packet_decrypt(md, priv_key):
    md = int(md)
    n = int(priv_key.split('_')[0])
    d = int(priv_key.split('_')[1])
    m = pow(md,d,n)
    m = h.convertFromNumber(m)
def decrypt(md,priv_key):
    md = md.split(".")
    for i in range(len(md)):
        md[i] = packet_decrypt(md[i],priv_key)
    m = "".join(md)
    return m

def verifyKeys(pub_key, priv_key):
    testMessage = "hi12"
    out = encrypt(testMessage,pub_key)
    out = decrypt(out,priv_key)
    return out == testMessage

key = 0

def main():
    if len(sys.argv) != 2:
        print("Specify e or d for encrypt or decrypt")
        return
    toggle = sys.argv[1]
    if toggle != "e" and toggle != "d":
        print("Invalid option")
        return

    with open('keys.txt','r') as keys:
        key = next(keys)
    with open('in.txt', 'r') as infile:
        contents = infile.read()
        out = 0 
        if toggle == "e":
            out = encrypt(contents,key)
        else:
            out = decrypt(contents,key)
        with open('out.txt', 'a') as outfile:
            outfile.write(out)

if __name__ == "__main__":
    main()
