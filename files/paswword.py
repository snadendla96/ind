#!/usr/bin/python

#here it will read the file which has given
psfile = open("/etc/passwd")
#here we print the psfile data
print psfile
#here soft variable is assigned to readlines()
#readlines will read the all the lines at onces onley in a list formate
soft = psfile.readlines()
#here print will print all the data in the list at onces
print soft
#the for i will loop the given data and it find the len of the file and it will print with length also and it will strip the empty spaces "\n"
for i in range(0,len(soft)):
      print i+1,soft[i].strip()