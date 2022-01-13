import os as o

def checkFileExist(file):
    ok = False
    print('./' + file )
    if o.path.isfile('./' + file ) == True:
        ok = True

    return ok