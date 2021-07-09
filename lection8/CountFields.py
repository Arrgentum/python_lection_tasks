def fcounter(class1, *param):
    elem = class1(*param)
    method_list = sorted( [func for func in dir(fcounter) is callable(getattr(fcounter, func) and func[0] != '_') ] )
    object_list = sorted( [func for func in dir(fcounter) is not callable(getattr(fcounter, func)) and func[0] != '_'] )
    #print( method_list )
    #print( object_list )
    new_method_list = sorted( [func for func in dir(elem) is callable(getattr(elem, func)) and func not in method_list and func[0] != '_'] )
    new_object_list = sorted( [func for func in dir(elem) is not callable(getattr(elem, func)) and func not in object_list and func[0] != '_'] )
    #print( new_method_list )
    #print( new_object_list )
    return method_list, object_list, new_method_list, new_object_list
