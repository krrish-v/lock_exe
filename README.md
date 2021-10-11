# locking program
This is a encryption program that is capable to encrypting password files of small size, it uses the RSA-4096 bit encryption to encrypt the file. It is completely build on python language contains PyCrypto and RSA libraries.

You have you have to convert this file into exe format

Before that download all the libraries given in [requirements.txt] file using pip, see in above directory

In terminal 

$ pip install pyinstaller

or

$ pip3 install pyinstaller

then open the directory where you downloaded these files in terminal

type - (basically to convert independent program that can run without python)

$ ./pyinstaller --onefile -w lock.py


- Delete all the extra created file except dist folder which contains exe file as named lock

HOW TO USE THIS EXE_FILE---------


Default Password - hail-kali


[1] open terminal from where you had downloaded a file.

[2] type the following command to start the program
$ ./lock

[3] It will ask you a password now type the deafult password given over

You can change it in the main file [lock.py], line 11
passsw = "your_password"

[4] now go accroding to the commands specified in the program


KEY POINTS (don't skip)

[SECURITY POINT] Move that private key file to somewhere else to any other stograge device, but keep it safe other you will never get that encrypted file again

you can use this exe file in your pendrive if you store some credentials over their in small sized file, it is basically for that purpose only

NOTE -- If you want to encrypt the file again after decrypting it, you have remove the encoded text from that
secret file otherwise it will not work, It will not affect anyhow, but don't touch the file after encrypting it. You can make changes after decryption.

|||||||||||||||||||||||||||||||||||||||||||||||||||||||

Its Drawbacks

[1] It cannot encrypt the large files



(Happy encrypting and decrypting).upper()
