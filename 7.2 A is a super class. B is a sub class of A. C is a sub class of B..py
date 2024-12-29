#7.2 A is a super class. B is a sub class of A. C is a sub class of B.

#Multilevel inheritance

class Iphone1:
    def display(self):
        print("display 15 inches")
    def camera(self):
        print("camera 15mg")
class Iphone2(Iphone1):
    def selfiecamera(self):
        print("selfiecamera")
class Iphone3(Iphone2):
    def facerecognisition(self):
        print("facerecognisition")
i3=Iphone3()
i3.camera()
i3.display()
i3.selfiecamera()
i3.facerecognisition()


