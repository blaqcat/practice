class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz =23

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar =  'overridden'
        self.__baz =  'overridden'
