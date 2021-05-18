# Lost in Transmission

![misc category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-75-blue.svg)

## Challenge:

I had my friend send me the flag, but it seems a bit...off.



## Solution:

Attached file
```
E6C8C6E8CCF6AE60DC8866E4CCAA98BEDAB2BE8E6060C8BEE662A4FA
```

It doesn't decode into anything particularly helpful.

[CyberChef's intensive mode](https://gchq.github.io/CyberChef/#recipe=Magic(3,true,false,'sdctf%7B')&input=RTZDOEM2RThDQ0Y2QUU2MERDODg2NkU0Q0NBQTk4QkVEQUIyQkU4RTYwNjBDOEJFRTY2MkE0RkE), combined with `sdctf{` as crib, helps us right away with right rotation from hex

Now we have the flag: `sdctf{W0nD3rfUL_mY_G00d_s1R}`.
