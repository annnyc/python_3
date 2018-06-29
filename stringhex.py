
import binascii
x=input("digite algo")
binascii.hexlify(bytes(x,"utf-8"))
for c in x:
    print("".join(hex(ord(c))[2:]))
