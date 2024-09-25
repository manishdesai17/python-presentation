#search mca,bca,pgdca student using roll no
from Hostal_managment.AddStudent import *
def getMcaStudent(mca,search):
    l=mca.keys()
    if(search in l):
       return mca[search]
    else:
        return False

#bca
def getBcaStudent(bca,search):
    l=bca.keys()
    if(search in l):
       return bca[search]
    else:
        return False

#pgdca
def getPgdcaStudent(pgdca,search):
    l=pgdca.keys()
    if(search in l):
       return pgdca[search]
    else:
        return False