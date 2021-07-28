# RSA Twins! 

https://mega.nz/#!2aBwFCKa!NWQKRIbYzSAU2iwCPNppO7SE92W6sne4FKD3sKE2A-k Aww, twins :). Theyâre so cute! They must be (almost) identical because theyâre the same except for the slightest difference. Anyway, see if you can find my flag. Hint: This is just math. You're probably not going to find any sort of specialized attack.

## Solution

A classic RSA challenge where p and q look alike. this was referred to as twin primes.
factorizing n using factordb and following the exploit I got the flag

```
from Crypto.Util.number import *

p = 121588253559534573498320028934517990374721243335397811413129137253981502291629
q = 121588253559534573498320028934517990374721243335397811413129137253981502291631

e = 65537

c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587

n = p*q

phi = (p-1)*(q-1)

d =  inverse(e,phi)

print(long_to_bytes(pow(c,d,n)))

```

flag
```
flag{i_l0v3_tw1N_pr1m3s}
```
