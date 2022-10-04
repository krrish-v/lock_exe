# locking program
This is a encryption program that is capable to encrypting password files of small size, it uses the RSA-4096 bit encryption to encrypt the file. It is completely build on python language contains PyCrypto and RSA libraries.


## This program is outdated

The updated one -
    https://github.com/krrish-v/hashent


You have you have to convert this file into exe format

Before that download all the libraries given in [requirements.txt] file

There will be highly chances that you will get the issue in pycrypto module

see here to solve the issues https://github.com/pycrypto/pycrypto/issues

SETUP TIME|||

In terminal -------

    $ pip install pyinstaller

    $ pip install crypto && pip install pycrypto && pip install pyautogui && pip install rsa

    $ ./pyinstaller --onefile -w lock.py

OVER|||

Go to the directory open the dist folder

NOTE - Delete all the extra created file except dist folder which contains exe file as named lock

HOW TO USE THIS EXE_FILE---------


Default Password - hail-kali


[1] open terminal command 

    $ cd path_name

[2] type the following command to start the program

    $ ./lock

[3] It will ask you a password now type the deafult password given over

You can change it in the main file [lock.py], line 12
passsw = "your_password"

[4] now go accroding to the commands specified in the program


(don't skip)

[SECURITY POINT] Move that private key file to somewhere else to any other stograge device, but keep it safe otherwise you will never get that encrypted file decrypted again

you can use this exe file in your pendrive if you store some credentials over their in small sized file, it is basically for that purpose only

NOTE -- If you want to encrypt the file again after decrypting it, you have remove the encoded text from that
secret file otherwise it will not work, It will not affect anyhow, but don't touch the file after encrypting it. You can make changes after decryption.

|||||||||||||||||||||||||||||||||||||||||||||||||||||||

Its Drawbacks

[1] It cannot encrypt the large files, which require chunking of data
