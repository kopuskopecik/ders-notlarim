> What is the full path of your home directory?

$ cd

$ pwd 

/home/luc

$ pwd -P

/home/luc


Or look in the "user database":

$ cat /etc/passwd


This works too:

$ echo ~

/home/luc


> Are there any files or directories in your home directory?

$ ls

$ ls -a

$ ls -A 


> Can you find your numerical user id?

You can assume you are the owner of your home directory

$ ls -ldn ~

drwxr-xr-x 28 1000 1000 4096 Jun  8 13:32 /home/luc


More direct ways:

$ id

uid=1000(luc) gid=1000(luc) [...]


Or look in the "user database":

$ cat /etc/passwd


> Are there any files in /usr/bin containing a number?

$ ls /usr/bin/*[0-9]*


> Create a directory called exercises in your home directory.

$ cd

$ mkdir exercises


> Copy /usr/bin/batch to this directory.

$ cp /usr/bin/batch exercises/


> What is the purpose of this command?

$ whatis batch

$ man batch


> What kind of file is it?

$ file exercises/batch

exercises/batch: POSIX shell script, ASCII text executable


> Are there any metadata differences between the original and the copy.

$ ls -l /usr/bin/batch exercises/batch


> Copy /usr/bin/batch to the exercises directory, under a different name

> (the choice is yours), but use option -p of command cp.


$ cp -p /usr/bin/batch exercises/batch2


> What is the purpose of option -p? 

$ man cp


> Is it working as intended? Can you explain?

A normal user should not be able to create files owned by somebody else.


> What is the size (in K) of the whole directory exercises?

$ du -ks exercises/


> What is the size (in K) of the last modified file in directory exercises?

$ ls -ltr --block-size=1024 exercises/

(the most recent entry is at the bottom of the list)


> Remove directory exercises.

$ rm -rf exercises/


> What are the permissions, owner and group of /?

$ ls -ld /


> Is there any difference between ‘ls’ and ‘ls *’?

When there is a subdirectory, ‘ls *’ will show the contents of that directory, while ls will not.