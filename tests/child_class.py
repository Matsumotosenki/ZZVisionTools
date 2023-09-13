"""
Author:Qychui
DATE:2023/9/13 14:39
File:child_class.py
"""
from parent_class import ParentClass  # 导入父类

class ChildClass(ParentClass):  # 子类继承父类
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类的构造函数
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")