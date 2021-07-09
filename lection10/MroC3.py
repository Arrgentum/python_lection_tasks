from re import *

string = input()
rec = ""
pas = " pass"
while bool(string):
	if match("class", string) : 
		if not search("pass", string):
			string += pas
		rec += (string + '\n')
	string = input()

flag = True
try:
	exec(rec)
except TypeError:
	flag = not flag

if flag:
	print("Yes")
else:
	print("No")