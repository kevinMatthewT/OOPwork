class Person:
    def __init__(self,name,address):
        self.__name=name
        self._address=address
    
    def setName(self,name):
        self.__name=name

    def setAddress(self,address):
        self._address=address

    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self._address
    
    def  __str__(self):
        return "{} ({})" .format(self.getName(),self.getAddress())

class Student(Person):
    def __init__(self,name,address,courses,grades):
        super().__init__(self)
        self.courses=courses
        self.grades=grades
    
    def addCourseGrade(self,courses,grades):
        CourseNames=()
        CourseNames.append(courses)
        GradesAmount=()
        GradesAmount.append(int(grades))
        self._Courses=CourseNames
        self._Grades=GradesAmount
        return self._Courses ,self._Grades
    
    def printGrades(self):
        print(self._Grades)

    def getAverageGrade(self):
        for i in self._Grades:
            total= total+ self._Grades
            i= i+1
        AverageGrade=total/len(self._Grades)
        return AverageGrade

    def __str__(self):
        return "{} ({})" .format(self.getName(),self.getAddress())

class Teacher(Person):
    def __init__(self,name,address,courses):
        super().__init__(self)
        self.courses=courses

    def addCourse(self,course):
        NamesCourses=()
        if course not in NamesCourses:
            NamesCourses.append(course)
        else:
            pass
        self.CourseList=NamesCourses
        return self.CourseList
    
    def removeCourse(self,course):
        if course in self.CourseList :
            NamesCourses=self.CourseList
            NamesCourses.remove(course)
            self.CourseList=NamesCourses
        else:
            pass
        return self.CourseList

    def __str__(self):
        return "{} ({})" .format(self.getName(),self.getAddress())

#here is my solution sir, but i dont know why the super() does not work, i also tried writing the name of the main class also
