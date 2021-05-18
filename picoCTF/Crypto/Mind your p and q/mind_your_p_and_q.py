
#!usr/bin/python3

from Crypto.Util.number import *
from sympy import factorint


#given values
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
e = 65537

p,q = factorint(n)

phi = (p-1)*(q-1)
d = inverse(e,phi)
flag = pow(c,d,n)
print(long_to_bytes(flag))
