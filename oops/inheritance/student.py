class student:
    def __init__(self,student_id,name,age,gender,course,branch,semester,marks,phone,email,password):
        self.student_id = student_id
        self.name = name
        self.__age = age
        self.gender = gender
        self.course = course
        self.branch = branch
        self._semester = semester
        self._marks = marks
        self.__phone = phone
        self.__email = email
        self.__password = password


    def display_student(self):
        print("Student_id : ",self.student_id)
        print("Name : ",self.name)       
        print("Gender : ",self.gender)
        print("Course : ", self.course)
        print("Branch : ",self.branch)
        print("Semester : ",self._semester)
        print("Marks : ",self._marks)


    def __private_details(self):
       print("Phone : ",self.__phone)
       print("Email : ",self.__email)
       print("Password : ",self.__password)

    def show_private_details(self):
        self.__private_details()

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


s =result(101,"Prince",22,"Male","B.Tech","CSE",8,68,7067405997,"prince@gmail.com",12345)
s.display_student()
s.show_private_details()
s.grade()
