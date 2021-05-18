# Strong password

![misc category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)

## Description
Zip file with a password. I wonder what the password could be? Hint: Don't use fcrackzip

[strong_password.zip]

## Solution

First get the hash file from the zip using
```
zip2john strong_password.zip > hash
```

then you will be getting 2 hashes in hash file so split the hashes and run them seperately with
```
john hash --wordlist=/usr/share/wordlists/rockyou.txt
```

and you will get the password
```
Bo38AkRcE600X8DbK3600
```

you will have a lorem ipsum file over there and using the following command I got the flag
```
cat lorem_ipsum.txt | grep dctf
```

flag:```dctf{r0cKyoU_f0r_tHe_w1n}```
