# Tux
The flag is hidden inside the Penguin! Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.

## Solution

use exiftool to get the base64 encoded string. decoding that will give you a password. then use

```
binwalk -e Tux.jpg
```

to extract the zip file from the image and use the password as the password of the zip file for tha flag

flag
```
CTFlearn{Linux_Is_Awesome}
```
