def TypeCheck(list_type1, type_elem):
	list_type = list(list_type1)
	def decorated(fun):
		def newfun(*args, **kwargs):
			if len(list_type) != len(args) + len(kwargs):
				#print(len("dfcvb" , list_type))
				raise TypeError("Function " + fun.__name__ + " must have " + str(len(list_type)) + " arguments")
				#raise TypeError('Function {1} must have {2} arguments'.format(fun.__name__, len(list_type)))

			for i in range(len(args)):
				if type(args[i]) is not list_type[i]:
					raise TypeError("Type of argument " + str(i+1) + " is not " + str(list_type[i]))
					#raise TypeError('Type of argument {1} is not {2}'.format(args[i], list_type[i]))

			for i, k in enumerate(kwargs.items()):
				if type(k[1]) is not list_type[i+len(args)]:
					raise TypeError("Type of argument '" + str(k[0]) + "' is not " + str(list_type[i+len(args)]))
					#raise TypeError('Type of argument {1} is not {2}'.format(j, list_type[i]))

			res = fun(*args, **kwargs)
			if type(res) is not type_elem:
				raise TypeError("Type of result is not " + str(type_elem))
				#raise TypeError('Type of result is not {}'.format(type_elem))
			return res

		return newfun
	return decorated