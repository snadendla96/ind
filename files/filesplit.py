#!/usr/bin/python
#it will read the file which has given
psfile = open("/etc/passwd")
#here we print the psfile data
print psfile
#here soft variable is assigned to readlines()
#readlines will read the all the lines at onces onley in a list formate
soft = psfile.readlines()
#here print will print all the data in the list at onces
#print soft[0].split(":")
#print soft[0].soft[0]

# soft[0].split(":")

jump = soft[0].split(":")
print  jump
print  "username->",jump[0] 
print "passwd->",jump[1]
print "UserId(UID)->",jump[2]
print "GroupId(GID)->",jump[3]
print "Userinfo->",jump[4]
print "Home directory->",jump[5]
print "command/shell->",jump[6].strip()
#the for i will loop the given data and it find the len of the file and it will print with length also and it will strip the empty spaces "\n"
#for i in range(0,len(soft)):
 #    print i+1,soft[i].strip().split(":")
#     print "user"soft[0]

     