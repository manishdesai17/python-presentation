#remove mca ,bca,pgdca student 
from Hostal_managment.AddStudent import *
def RemMcaStudent(mca,rem):
    l=mca.keys()
    if(rem in l):
         del mca[rem]
         return True

#bca
def RemBcaStudent(bca,rem):
    l=bca.keys()
    if(rem in l):
         del bca[rem]
         return True

#pgdca
def RemPgdcaStudent(pgdca,rem):
    l=pgdca.keys()
    if(rem in l):
         del pgdca[rem]
         return True