## encoding UU

So this also similar to that of encoding ASCII challenge but here the encoding type is UU. I would appreciate them
as they tried giving the challenge in UU encryption as it was not widely used in CTFS and not widely known by the
beginners. Jumping into the challenge same like previous one we have the clue in the challenge name itself.
The problem statement was to get the validation password(which is basically the flag in this case).Under the
problem statement there was a link which led to a webpage containing some text along with the cipher text. This
was present in that webpage:
=_
_=_ Part 001 of 001 of file root-me_challenge_uudeview
_=_
begin 644 root-me_challenge_uudeview
B5F5R>2!S:6UP;&4@.RD*4$%34R\`](%5,5%)!4TE-4$Q%"@\``
`
end
the line below the line starting with begin is the ciphertext which is easily identifiable. As the name hints same as
the previous one without any second thoughts I went for an decoding this on my linux terminal.
And for those who dont know what UU encoding is... UU encoding is a basic unix to unix encoding which can be
used to encode binary data into ASCII ones.
For decoding it with the linux terminal one should have the package named “sharutils” which contains both
uuencode and uudecode functions. so for installing it we have to run the command
sudo apt-get install sharutils

![euu1](https://user-images.githubusercontent.com/55373148/116653628-3a6f4200-a9a5-11eb-880b-bc2e5e923500.png)


then after installing this package I copied the text from beign to end and pasted in a file named ch1.txt as that is
the format of the file. Then by using the command
uudecode -o result ch1.txt;cat result
we can get the deoded string which displayed

![euu2](https://user-images.githubusercontent.com/55373148/116653636-3f33f600-a9a5-11eb-8e37-da6bd01afa51.png)


So we can use the password provided here to validate the one in the site. Here uudecode is used for decoding unix
to unix and -o is used for copying the answer in result and cat result is used to add the answer to your
terminal.Easy pie :)

