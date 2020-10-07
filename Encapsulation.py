

class Robot(object):
   def __init__(self):
      self.a = "I"
      self._b = "am"
      self.__c = " a Robot"

   def getc(self):
       print(self.__c)

   def setc(self, c):
       self.__c = c
       
if __name__ == "__main__":
    obj = Robot()
    print(obj.a)
    print(obj._b)
    obj.getc()
    obj.setc("not a Robot")
    obj.getc()
    print(obj.__c)

