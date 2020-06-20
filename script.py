import shutil
import os, os.path
from os import listdir
from os.path import isfile, join
import pyzipper
import sys
import time
import zipfile

def clear(): return os.system('cls')

def receive_input():
    clear()
    while 1:
        pasta = input("Insira o caminho que tem os ficheiros zip->")
        ficheiros = []

        if os.path.exists(pasta):
            break
        else:
            print("O caminho que inserio é inexistente!")

    for f in listdir(pasta):
        if isfile(join(pasta,f)):
            if ".zip" in f or ".rar" in f:
                ficheiros.append(f)

    if len(ficheiros) < 1:
        while 1:
            resposta = input("Não existem ficheiros zip nesta pasta, pretende escolher outra? (S/N)->")
            if str(resposta.lower()) == "s":
                receive_input()
                break
            elif str(resposta.lower()) == "n":
                sys.exit(0)
    else:
        while 1:
            manter = input("Pretende deixar o programa a encriptar todos os ficheiros zip nesta pasta? (S/N)->")
            if str(manter.lower()) == "s":
                zip_it(pasta, ficheiros, True)
                break
            elif str(manter.lower()) == "n":
                zip_it(pasta, ficheiros, False)
                break

def zip_it(p, f, k):
    clear()
    if not k:
        try:
            if not os.path.exists(p + "\\_1"):
                os.mkdir(p + "\\_1")

            pwd = b'mvti1234mvti1234'

            for i in range(len(f)):
                print("Falta encriptar " + str(len(f) - i) + " ficheiros")
                foo = p + "\\_1\\" + f[i]
                with pyzipper.AESZipFile(foo,'w',compression=pyzipper.ZIP_LZMA) as zf:
                    zf.pwd = pwd
                    zf.setencryption(pyzipper.WZ_AES, nbits=128)
                    zf.write(p + "\\" + f[i], os.path.basename(p + "\\_1\\" + f[i]))
            for i in range(len(f)):
                os.remove(p + "\\" + f[i])

            print("Todos os ficheiros foram encriptados")
        except Exception as ex:
            print(ex)
            pass
    else:
        count = 0
        while 1:
            try:
                if not os.path.exists(p + "\\_1"):
                    os.mkdir(p + "\\_1")

                pwd = b'mvti1234mvti1234'

                for i in range(len(f)):
                    count += 1
                    print("Foram encriptados " + str(count) + " ficheiros")
                    foo = p + "\\_1\\" + f[i]
                    with pyzipper.AESZipFile(foo,'w',compression=pyzipper.ZIP_LZMA) as zf:
                        zf.pwd = pwd
                        zf.setencryption(pyzipper.WZ_AES, nbits=128)
                        zf.write(p + "\\" + f[i], os.path.basename(p + "\\_1\\" + f[i]))
                for i in range(len(f)):
                    os.remove(p + "\\" + f[i])

                f = []

                for ff in listdir(p):
                    if isfile(join(p,ff)):
                        if ".zip" in ff or ".rar" in ff:
                            f.append(ff)

                time.sleep(15)    
            except Exception as ex:
                print(ex)
                pass        

receive_input()