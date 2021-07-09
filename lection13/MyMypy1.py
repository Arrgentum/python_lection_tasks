from functools import wraps
import inspect

def check(func):
    info = inspect.getfullargspec(func)
    position_or_keyword = info.args
    position_or_keyword.remove("self")
    kwonlyargs = info.kwonlyargs
    varargs = info.varargs
    varkw = info.varkw
        # print("$$$:", info)
        # print("$$$:", position_or_keyword, kwonlyargs, varargs, varkw)
    parametrs_dict = dict()

    @wraps(func)
    def newfunc(self, *args, **kwargs):
        sig_info = inspect.signature(func)
        bind_info = sig_info.bind(self, *args, **kwargs)
            # print(">>>", type(sig_info), sig_info)
            # print(">>>", type(bind_info), bind_info)
        func_parametrs = sig_info.parameters

        for key, value in bind_info.arguments.items():
            # print(key, value, sig_obj.parameters[key])
            # print(sig_obj.parameters[key].annotation)
            if sig_info.parameters[key].annotation is not sig_info.empty:
                parametrs_dict[key] = [value, sig_info.parameters[key]]

        index = flag = 0
        for j in position_or_keyword:
            if j in parametrs_dict:
                compare_with = parametrs_dict[j][1].annotation
                if not isinstance(args[index], compare_with):
                    raise TypeError(f"Type mismatch: {j}")
            if len(args) > index + 1:
                index += 1
            else:
                amount = len(position_or_keyword[index + 1:]) + len(kwonlyargs)
                for number, i in enumerate(kwargs):
                    if i in parametrs_dict:
                        compare_with = parametrs_dict[i][1].annotation
                        if not isinstance(kwargs[i], compare_with):
                            raise TypeError(f"Type mismatch: {i}")
                    elif i == varargs:
                        compare_with = func_parametrs[varargs].annotation
                        if not isinstance(kwargs[i], compare_with):
                            raise TypeError(f"Type mismatch: {varargs}")
                    elif number == (amount - 1):
                        break
                for i in kwargs:
                    compare_with = parametrs_dict[varkw][1].annotation
                    if not isinstance(kwargs[i], compare_with):
                        raise TypeError(f"Type mismatch: {varkw}")
                flag = 1
                break
        if flag == 0:
            for i in kwonlyargs:
                if i in parametrs_dict:
                    compare_with = parametrs_dict[i][1].annotation
                    if not isinstance(kwargs[i], compare_with):
                        raise TypeError(f"Type mismatch: {i}")
            if varargs in parametrs_dict:
                for i in args[index:]:
                    compare_with = parametrs_dict[varargs][1].annotation
                    if not isinstance(i, compare_with):
                        raise TypeError(f"Type mismatch: {varargs}")
            elif varkw in parametrs_dict:
                for i in kwargs:
                    compare_with = parametrs_dict[varkw][1].annotation
                    if not isinstance(kwargs[i], compare_with):
                        raise TypeError(f"Type mismatch: {varkw}")

        if sig_info.return_annotation != sig_info.empty:
            if not isinstance(func(self, *args, **kwargs), sig_info.return_annotation):
                raise TypeError("Type mismatch: return")

        return func(self, *args, **kwargs)
    return newfunc


class checked(type):
    def __init__(self, Name, Parents, Dict):
        super().__init__(Name, Parents, Dict)
        # print(Dict)
        for key, value in Dict.items():
            # value is function
            if key != "__init__" and callable(value):
                # print(">>>", key, ">>>", value, ">>>", inspect.getfullargspec(value))
                setattr(self, key, check(value))
