
## File PKZIP

This Challenge is a pretty interesting one.The problem statement was to check what's inside a protected zipile
without password provided. So basically the challenge here is to crack the password of the ZIP file. Below the
problem statement I had the link for downloading the zip file.</br>
I was thinking for a while regarding the approach and finally came to a decision to Use fcrackzip in John. So at first
we have to run the following commands
```
sudo apt update
```
this command is for downloading package information of all the configured sources.Then
```
sudo apt install john fcrackzip wordlists
```
this command is used for downloading all the wordlists which we use to find the password of the ZIP file.Then we
have to locate the wordlists so for that
```
locate wordlists
```

![PKZIP1](https://user-images.githubusercontent.com/55373148/116654193-4dcedd00-a9a6-11eb-8ee0-39a667314beb.png)

This will display all directories with path wordlists so the list will be too long from this we need rockyou.txt which is the basic and important wordlists file and I finally found it in the bottom of the list but as a gz file./usr/share/wordlists/rockyou.txt.gz</br>

gz ( GunZip) is a type of zipfile which we again need to extract in order to get rockyou.txt so I used the following
command for unzipping
```
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
```
after running this I got rockyou.txt so I started bruteforcing the content in rockyou.txt for finding the correct
password with the following command
```
fcrackzip -v -D -u -p /usr/share/wordlists/rockyou.txt ch5.zip
```
in this command fcrackzip is the base package and -v is used for Validation, -D is used to access dictionary, -u is
used to unzip the file and -p is used for using string as an initial password.
after running this command it usually takes few minutes to get you the answer and I finally got the password
![PKZIP2](https://user-images.githubusercontent.com/55373148/116654210-53c4be00-a9a6-11eb-8988-1fbb4a6f5bb6.png)





