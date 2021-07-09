class Nuts:

    def __init__(self, *argc):
        pass

    def __str__(self):
        return "Nuts"

    def __getitem__(self, key):
        return key

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __getattr__(self, name):
        return name

    def __setattr__(self, name, value):
        pass

    def __delattr__(self, name):
        pass

    def __iter__(self):
        return iter(tuple())
