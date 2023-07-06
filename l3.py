"""
    面向对象编程
"""


class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self.name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self._age = age

    def __age(self):
        print(f'{self._name}不想不想长大，长大后就没童话')

    def study(self, course_name):
        print(f'{self._name}，{self._age} 正在学习 {course_name}')
        self.__age()


def main():
    stu = Student('佩奇', 24)
    stu.age(19)
    stu.study('洗澡攻略')
