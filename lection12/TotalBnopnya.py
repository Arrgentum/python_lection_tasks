from string import *

def analysis_string(ans, cur, Dict, name):
	if cur == 3 :
		for i, j in Dict.items():
			if not j:
				print(i, end = " ")
	print(name)
	print(ans)
	alphabet = "ПABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНЕОРСТУФХЦЧШЩЫЭЮЯ()[]+-*/%;.,>=<\"!:"
	alp = alphabet.encode('koi8-r')
	if ans[:1] = [:1]
	for i in ans:
		if i not in alp:
			return None
	print(ans)
	return ans


def analysis(cur, Dict, string, name):
	if cur == 5 :
		return None
	if name:
		if isinstance(string, bytes):
			try:
				string = string.decode(name)
				if analysis_string(string, cur, Dict, name):
					return string
			except:
				pass
		elif isinstance(string, str):
			try:
				string = string.encode(name)
			except:
				pass
		Dict[name] = False

	for i, j in Dict.items():
		if j:
			Y = Dict.copy()
			flag = analysis(cur + 1, Y, string, i)
			if flag:
				return flag


D = {i : True for i in input().split()}
string = bytes.fromhex(input())
print(analysis(0, D, string, None))