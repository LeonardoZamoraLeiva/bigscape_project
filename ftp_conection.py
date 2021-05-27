import os
from ftplib import FTP

host_address = 'ftp.ncbi.nlm.nih.gov'
user_name = 'anonymous'
password = 'leo.zamoraleiva@gmail.com'
ftp = FTP(host_address)
ftp.login(user=user_name, passwd=password)


def FTP_Walker(FTPpath, localpath):
    os.chdir(localpath)
    current_loc = os.getcwd()
    for item in ftp.nlst(FTPpath):
        if not is_file(item):
            yield from FTP_Walker(item, current_loc)

        elif is_file(item):
            yield item
            current_loc = localpath
        else:
            print('this is a item that i could not process')

    os.chdir(localpath)
    return


def StrainName(FTPpath):
    strain_name = []
    for item in range(len(ftp.nlst(FTPpath))):
        listPath = ftp.nlst(FTPpath)[item].split(os.sep)
        strain = listPath[5]
        strain_name.append(strain)
    return strain_name


def is_file(filename):
    current = ftp.pwd()
    try:
        ftp.cwd(filename)
    except Exception as e :
        ftp.cwd(current)
        return True

    ftp.cwd(current)
    return False


def ask_strain(strainCollection):
    strains = False
    while not strains:
        strain = str(input('Please enter the strain you want (eg:Streptomyces_albidoflavus): '))
        strainCollection.append(strain)

        question = str(input('Want to add more strains? (Y/N): '))
        if 'n' in question.lower():
            strains = True