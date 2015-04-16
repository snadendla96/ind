#!/usr/bin/python
cast= ["clease","Palin","Jones","Idle"]
print cast 

print(len(cast))
#here it will print the number words length in cast 

print (cast[1])
#It will print the "1" word in list that is "Pali
#if u wan't append a ny data to the existing list use the following method

cast.append("Gillam")
print cast

#here the append is used to a string to the existing list

cast.pop()
print cast
#pop will delete one string from the list

cast.extend(["Gillam,Chapman"])
print cast
#extend will help in adding the word to existing list

cast.remove("Chapman") 
print cast

#remove is used to remove a string from the list


cast.insert(0,"Chapman") 
print cast
#insert is used to insert the string in particular place in a list here we can added in the middle of the list also by giving the index number

dir(list)
#you can use dir(list) fro help 

cast.index("Champman")
print cast
#in this it will show the index number of given string

cast.append("Champman")
cast

cast.count("Champman")
print cast
#count is used to count the a string how many times it has occurence of a word in list 


cast.sort()
#it will sort the order of the list in ascending or in desending order
