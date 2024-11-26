from Hostal_managment.AddStudent import *
from Hostal_managment.SearchStudent import *
from Hostal_managment.RemoveStudent import *
mca={}
bca={}
pgdca={}

while(True):
#    hostel managment operation
   print("1.Add student in Hostel:")
   print("2.Search student in Hostel:")
   print("3.Remove student in Hostel:")
   print("4.exit")
   c=int(input("Enter choice:"))
   if(c==1):
       while(True):
         print("1.Add mca student:")
         print("2.Add bca student:")
         print("3.Add pgdca student:")
         print("4.exit")
         c1=int(input("Enter choice:"))
          #add mca student
         if(c1==1):
           roll_no=input("\nEnter MCA student roll no:")
           name=input("Enter MCA student name:")
           print("Add MCA student ",addMcaStudent(roll_no,name,mca),"successfully....")

         #add bca student
         elif(c1==2):
           roll_no=input("\nEnter BCA student roll no:")
           name=input("Enter BCA student name:")
           print("Add BCA student ",addBcaStudent(roll_no,name,bca),"successfully....")
 
        #add pgdca student
         elif(c1==3):
            roll_no=input("\nEnter PGDCA student roll no:")
            name=input("Enter PGDCA student name:")
            print("Add PGDCA student ",addPgdcaStudent(roll_no,name,pgdca),"successfully....")
         elif(c1==4):
             break
   elif(c==2):
       while(True):
          print("1.Search MCA student")
          print("2.Search BCA student")
          print("3.Search PGDCA student")
          print("4.exit")
          c1=int(input("Enter choice:"))

       #search mca student
          if(c1==1):
             search=input("\nenter MCA student roll no you want to search:")
             print("=======MCA Student========")
             s=getMcaStudent(mca,search)
             if(s!=False):
                print("Student Name is :",s)
             else:
                 print("Student not found")

      #search bca student
          elif(c1==2):
             search=input("\nenter BCA student roll no you want to search:")
             print("=======BCA Student========")
             s1=getBcaStudent(bca,search)
             if(s1!=False):
                print("Student Name is :",s1)
             else:
                print("Student not found")
     #search pgdca student
          elif(c1==3):
             search=input("\nenter PGDCA student roll no you want to search:")
             print("=======PGDCA Student========")
             s1=getPgdcaStudent(pgdca,search)
             if(s1!=False):
                 print("Student Name is :",s1)
             else:
                 print("Student not found")

          elif(c1==4):
             break
   elif(c==3):
      while(True):
          print("1.remove MCA student")
          print("2.remove BCA student")
          print("3.remove PGDCA student")
          print("4.exit")
          c1=int(input("Enter choice:"))

 #remove mca student
          if(c1==1):
             rem=input("\nEnter MCA student roll no you want to remove:")
             rem1=RemMcaStudent(mca,rem)
             if(rem1==True):
                 print("MCA student remove successfully....")
             else:
               print("Data not present..") 

#remove bca student
          elif(c1==2):
             rem=input("\nEnter BCA student roll no you want to remove:")
             rem1=RemBcaStudent(bca,rem)
             if(rem1==True):
                 print("BCA student remove successfully....")
             else:
                 print("Data not present..")
#remove pgdca student
          elif(c1==3):
             rem=input("\nEnter PGDCA student roll no you want to remove:")
             rem1=RemPgdcaStudent(pgdca,rem)
             if(rem1==True):
                print("PGDCA student remove successfully....")
             else:
               print("Data not present..")

          elif(c1==4):
             break
   elif(c==4):
      break
   







