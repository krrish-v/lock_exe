# lock
This is a encryption program that is capable to encrypting password files of small size, it uses the RSA-4096 bit encryption to encrypt the file. It is completely build on python language contains PyCrypto and RSA libraries.

First of all you have you have to conver this file into exe format

Before that download all the libraries given in requirement.txt file

In terminal 

$ pip install pyinstaller

or

$ pip3 install pyinstaller

then open the directory where you downloaded these files in terminal

type - 

$ ./pyinstaller --onefile -w lock.py


- Delete all the extra created file except dist folder which contains exe file as named lock

HOW TO USE THIS EXE_FILE---------


Default Password - hail-kali


[1] open terminal from where you had downloaded a file.

[2] type the following command to start the program
$ ./lock

[3] now go accroding to the commands specified in the program


Happy encrypting and decrypting

NOTE -- If you want to encrypt the file again after decrypting it [file.txt], you have remove the encoded text from the file otherwise it will not work.

|||||||||||||||||||||||||||||||||||||||||||||||||||||||
Its Drawbacks

[1] It cannot encrypt the large files
