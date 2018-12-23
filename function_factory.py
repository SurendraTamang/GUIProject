#! /usr/bin/env python
'''
factory method for creating functions
'''

class TaskFunction(object):
    def factory(type):
        if type == "F1":
            return F1()
        if type == "F2":
            return F2()
        if type == "F3":
            return F3()
        if type == "F4":
            return F4()
        if type == "F5":
            return F5()
        if type == "F6":
            return F6()
        assert 0, "Bad Function: " + type

    factory = staticmethod(factory)

class F1(TaskFunction):
    def call(self, area, skill, size, is_senior, message):
        print("F1 Called")
        print("Area: ", area)
        print("skill: ", skill)
        print("size: ", size)
        print("is_senior: ", is_senior)
        print("message: ", message)

class F2(TaskFunction):
    def call(self, area, skill, size, is_senior, message):
        print("F2 Called")
        print("Area: ", area)
        print("skill: ", skill)
        print("size: ", size)
        print("is_senior: ", is_senior)
        print("message: ", message)

class F3(TaskFunction):
    def call(self, area, skill, size, is_senior, message):
        print("F3 Called")
        print("Area: ", area)
        print("skill: ", skill)
        print("size: ", size)
        print("is_senior: ", is_senior)
        print("message: ", message)

class F4(TaskFunction):
    def call(self, area, skill, size, is_senior, message):
        print("F4 Called")
        print("Area: ", area)
        print("skill: ", skill)
        print("size: ", size)
        print("is_senior: ", is_senior)
        print("message: ", message)

class F5(TaskFunction):
    def call(self, area, skill, size, is_senior, message):
        print("F1 Called")
        print("Area: ", area)
        print("skill: ", skill)
        print("size: ", size)
        print("is_senior: ", is_senior)
        print("message: ", message)

class F6(TaskFunction):
    def call(self, area, skill, size, is_senior, message):
        print("F6 Called")
        print("Area: ", area)
        print("skill: ", skill)
        print("size: ", size)
        print("is_senior: ", is_senior)
        print("message: ", message)
