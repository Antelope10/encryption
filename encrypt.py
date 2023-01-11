import random
import helper as h

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

def verifyKeys(pub_key, priv_key):
    testMessage = "hi12"
    out = encrypt(testMessage,pub_key)
    out = decrypt(out,priv_key)
    return out == testMessage

pub_key = 0
priv_key = 0

def main():
    contents = ""
    with open('in.txt', 'r') as infile:
        for line in infile:
            return
        with open('file.txt', 'w') as outfile:
            outfile.write('Hello World!')

    
if __name__ == "__main__":
    main()
