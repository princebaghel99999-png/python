class student:
    def __init__(self,name,marks,password):
        self.name = name 
        self._marks = marks
        self.__password = password


    def display(self):
        print("name : ", self.name)
        print("marks : ", self._marks)

    def __checkpassword(self):
        print("password : ",self.__password)

    def login(self):
        self.__checkpassword()


class result(student):
    def grade(self):

        if self._marks >=90:
            print("Grade A")
        elif self._marks >=80:
            print("Grade B")
        elif self._marks >= 70:
            print("Grade C")
        elif self._marks >= 60:
            print("Grade D")
        elif self._marks >= 50:
            print("Grade E")
        else:
            print("Fail")


s = result("ram", 85,'123456')
s.display()
s.grade()
s.login()