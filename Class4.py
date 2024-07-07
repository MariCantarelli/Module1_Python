#Working with String and Integers

#Marina is 19 years old and lives in the city of Recife.

Name = "Marina" #String
Age = 19 #Integer
#Age = str(Age) is a way to change Integer do String before the print 
City = "Recife" #String

#print(Name + "is" + Age + "years old and lives in the city of " + City + ".")
#Problem: can only concatenate str (not "int") to str

print(Name + " is " + str(Age) + " years old and lives in the city of " + City + ".")
#Not possible to put different types of data in the same print! 