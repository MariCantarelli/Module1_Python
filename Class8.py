#Format Strings

#Marina Cantarelli is an excellent [programmer]

Name = 'Marina'
Subname = 'Cantarelli'
Profession = 'Programmer'

Text = Name + " " + Subname + ' is an excellent [' + Profession + ']' 
print(Text)
Text2 = f'{Name} {Subname} is an excellant [{Profession}]' #Always iniciate with f' and ends with '
print(Text2)