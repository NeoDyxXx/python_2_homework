class MyStr(str):
    def is_repeatance(self, s: str):
        if self.__len__() % s.__len__():
            return False

        while True:
            if self.__len__() <= s.__len__():
                if self == s:
                    return True
                else:
                    return False
            s += s

    def is_palindrom(self):
        if not self:
            return True
        elif self.lower() == self[::-1].lower():
            return True
        else:
            return False



s = MyStr("HelloHello")
print(s.is_repeatance("Hello12141241241214124124"))

s = MyStr("madAm")
print(s.is_palindrom())