
from Crypto.PublicKey import RSA 
#change the package file {time.clock() to time.time()} line 77
from Crypto import Random
import rsa
import time
from pyautogui import alert, password
import sys



passsw = "hail-kali"


def pas():
    print('[*]\n Default Password ::\n')
    inp_p = password()
    if inp_p == passsw:
        print('\n[*] Correct Password _/\n')
        pass
    else:
        print('\n[-] Wrong (Default) Password /\ \n')
        print('\n [*] See the default password from')
        print('https://it-inosec.blogspot.com/2021/08/open-source-programs.html\n')
        sys.exit()


def keys_gen():
    try:
        typ = 4096
        key = RSA.generate(typ)
        #public key gen
        f = open('public-key.pem', 'wb')
        f.write(key.publickey().exportKey('PEM'))
        f.close()
        time.sleep(0.2)
        #private key gen
        f3 = open('private_key.pem', 'wb')
        f3.write(key.exportKey('PEM'))
        f3.close()
    except:
        print("\n[-] Unexprcted error in generating keys\n")
        sys.exit()


def get_pukey(): #checking a file
    try:
        f4 = open('public-key.pem', 'rb')
        key = RSA.importKey(f4.read())
        # getting the key
        print('\nusing stored encryption key\n')
        return key
    except FileNotFoundError:
        print('\n No key are been generated!!\n')
        print('\n[*]Generatina a key\n')
        time.sleep(0.1)
        print('          [*] Writing a RSA key [4096]------------------------------------\n[*] WAIT FOR IT...')
        time.sleep(0.2)
        keys_gen()
        print('\n[*] Keys generated___')
        print('[*] See those generated file named [lock_pub.pem, key_priv.pem]\n')
        return get_pukey()
    f4.close()


def get_prkey(): #checking a file
    try:
        f1 = open('private_key.pem', 'rb')
        key1 = RSA.importKey(f1.read())
        # getting the key
        print('\n[*] Collecting stored encryption key\n')
        return key1
    except FileNotFoundError:
        print('\n[-] KEY  [key(priv).pem file] is not present\t ')
    f1.close()


def renc(message): #message is a string that has to be encrypted
    print('[*] Encrypting your files...\n')
    key = get_pukey() # public key of encryption
    m = message.encode('utf-8')
    #print(m)
    x = rsa.encrypt(m, key)
    #print('your encrypted_text is : {}'.format(encrypted_text))
    print('[*] Encryption done\n')
    return x


def rdec(message): # message is a encrypted string
    print('[*] Decrypting your files...\n')
    key1 = get_prkey() # private key of a decryption
    z = key1.decrypt(message)
    #print('your decrypted_text is : {}'.format(decrypted_text))
    print('[*] Decryption done\n')
    return z


def fileenc():
    print('\n[*] Start Encrypting your files...\n')
    print('[*] If its is in other directories, enter the whole directory [NOTE]- Seperate it with commas]')
    filen = input('[*] Enter the place of files => ')
    print('\n[*] {' + filen + '} are been selected\n')
    filn = filen.replace(' ', '')
    tup = filn.split(",")
    for i in range(0, len(tup)):
        fna = tup[i]
        try:
            with open(fna, 'r') as f:
                msg = f.read()
                text = renc(msg)
                #print(text)
                e = open(fna, 'wb')
                e.write(text)
                e.close()
                f.close()
        except FileNotFoundError:
            print('\n[*]' + fna + ' file not found')


def filedec():
    print('\n[*] Start Decrypting your files...\n')
    print('[*] If its is in other directories, enter the whole directory [NOTE]- Seperate it with commas]')
    filen = input('[*] Enter the place of files => ')
    filn = filen.replace(' ', '')
    tup = filn.split(",")
    for i in range(0, len(tup)):
        fna = tup[i]
        try:
            with open(fna, 'rb') as f:
                msg = f.read()
                #print(msg)
                text = rdec(msg)
                #print(text)
                e = open(fna, 'wb')
                e.write(text)
                e.close()
                f.close()
        except FileNotFoundError:
            print('\n[*]' + fna + ' file not found')


def m():
    j = input('\n[*] So, "e" for encrypt|"d" for decrypt|type["exit"or"quit"or"q"] to exit the program \n=>')
    if 'e' == j or 'encrypt' == j:
        try:
            fileenc()
        except:
            print('\n[-] process not made try again!!\n')
        return m() #restart the whole process again
    elif 'd' == j or 'decrypt' == j:
        try:
            filedec()
        except:
            print('\n[-] process not made, try again----')
            print('[*]check weather all the credentials are in the directory or not\n')
        return m()
    elif 'exit' == j or 'quit' == j or 'q' == j:
        print('\n\n[*] Goodbye, have a nice encrypting day\n')
        alert("Star this program on GitHub <^>\nhttps://github.com/krrish-dev/lock_exe")
        print('link - https://github.com/krrish-dev/lock_exe\n')
        sys.exit()
    else:
        print('\n[-] Choose the correct option idiot')
        print('\n[*] try again ---')
        return m()


def main():
    print('\nENCRYPT TO HASH [RSA 4096]')
    logo = '''\n\n
    ###########################################################################
    #        ##  ##### ##       ##      ##       ##       #####################
    ####  ##### # #### ## ##### ## ####### ######## ###############   #####   # 
    ####  ##### ## ### ## ##### ## ####### ######## ##############   #####   ##
    ####  ##### ### ## ## ##### ##      ##       ## ##########                #
    ####  ##### #### # ## ##### ####### ## ######## ############   #####   ####
    ####  ##### #####  ## ##### ####### ## ######## ########                ###
    #        ## ###### ##       ##      ##       ##       ####   #####   ######
    #########################################################   #####   #######
    ###########################################################################
    '''
    print(logo)
    print('\t\t -- by an Indian Developer\n')
    pas()
    print('[*] Loading ...')
    time.sleep(1)
    print('\n[*] Weather you want to encrypt or decrypt|\n')
    m()


if __name__ == '__main__':
    main()
