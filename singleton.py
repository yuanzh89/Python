# Method 1: Overridding __new__
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.value = value

s1 = Singleton('first_instance')
s2 = Singleton('second_instance')

print(f"{s1 is s2=}")
print(f"{s1.value=}")
print(f"{s2.value=}")


# Method 2: Using a metaclass
class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]

class MySingleton(metaclass=SingletonMeta):
    def __init__(self, data):
        self.data = data

ms1 = MySingleton('data_one')
ms2 = MySingleton('data_two')

print(f"{ms1 is ms2=}")
print(f"{ms1.data=}")
print(f"{ms2.data=}")