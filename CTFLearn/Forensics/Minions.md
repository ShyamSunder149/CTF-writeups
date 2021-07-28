# Minions 
Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there: https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg Can you help me? TIP: Decode the flag until you got a sentence.

## Solution

follow that link to get a image. use 
```
binwalk -e filename 
```
to extract the contents of the image and you will have a .rar file. then unrar the file using
```
unrar -e filename
```
then you will get a link which lead you to the another image.use the same process and you will get an another image from the rar file
use strings for that image u will get a base64 encoded flag.decoding that 4 times with base64 will get you the flag

flag
```
CTF{M1NI0NS_ARE_C00L}
```
