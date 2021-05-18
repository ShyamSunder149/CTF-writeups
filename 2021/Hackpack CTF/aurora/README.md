
# Aurora

![misc category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Challenge:

Aurora is a marvelous phenomenon caused by the interaction between strong solar wind and magnetosphere around the earth.

Image source: https://science.nasa.gov/flag-shaped-aurora-over-sweden

## Solution:

We're given an image of an aurora:

<img src="Aurora.jpg" alt="Amazing" width="600">

A simple command reveals our flag:

```
$ strings Aurora.jpg | grep flag
flag{6e4ut1fuL_Aur0r4}
```

There it is, localized entirely within this CTF: `flag{6e4ut1fuL_Aur0r4}`.
