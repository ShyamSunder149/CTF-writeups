## Hash SHA 2

Hash SHA 2
This challenge is basically a hash cracking challenge as that of previous name and while seeing the challenge its
clear that we should make use of SHA (Secure Hash Alogorithm). This was written in problem statement:</br>
This hash was stolen during a session interception on a critical application, errors may have occurred during
transmission. No crack attempt has resulted so far; hash format seems unknown. Find the corresponding plaintext.
The answer is the SHA-1 of this password.</br>
A link was given below which led to a webpage containing the hash.The hash was the following one:
96719db60d8e3f498c98d94155e1296aac105ck4923290c89eeeb3ba26d3eef92</br>
I tried cracking this in almost always possible and finally found something is wrong with this. Then I was googling
about this and thanks to zyjsuper who pointed out that the hash is incorrect by stating the correct hash in one of
the forums.So the correct hash is:</br>
96719db60d8e3f498c98d94155e1296aac105c4923290c89eeeb3ba26d3eef92</br>
Then I went for cracking this hash in crackstation.net and got the password...

![sha1](https://user-images.githubusercontent.com/55373148/116653977-de58ed80-a9a5-11eb-925f-a7e5a9065d3f.png)


Then by reading the problem statement we got to know that the flag or validation password is the SHA1 encryption
of this password which is 4dM1n here So I went with terminal to encrypt the password by using the following
command.

```
echo -n 4dM1n | sha1sum
```

![sha2](https://user-images.githubusercontent.com/55373148/116653986-e31da180-a9a5-11eb-8c05-00ba49f95e27.png)



