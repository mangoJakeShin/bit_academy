import os

def sizechecker(path):
    filesize = 0
    if os.path.isdir(path):
        list = os.listdir(path)
        for files in list:
            myfile = os.path.join(path,files)
            # print(myfile)
            if os.path.isfile(myfile):
                filesize += os.path.getsize(myfile)
            elif os.path.isdir(myfile):
                subsize = sizechecker(myfile)
                filesize += subsize
    return filesize
