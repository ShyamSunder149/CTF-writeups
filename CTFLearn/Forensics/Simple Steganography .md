# Simple Steganography

Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"

## Solution

use strings to get the password for steghide and use steghide to extract the flag using the command
```
steghide extract -sf Minions1.jpeg
```
then you will get a base64 encoded flag on decoding gives flag
```
CTFlearn{this_is_fun}
```
